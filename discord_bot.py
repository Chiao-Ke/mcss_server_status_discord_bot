import discord
import asyncio
from datetime import datetime
import requests

# Settings Start:
# Discord Settings
CHANNEL_ID = 000000000000000000  # The channel you want bot to send message to
BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN"  # could be copy from your discord deeveloper portal

# Discord Bot Settings
BOT_STATUS = discord.Status.idle  # "idle" could be replaced by online, offline, idle, dnd, invisible
DISCORD_GAME = "Minecraft"  # the game that bot playing
UPDATE_PERIOD = 57  # seconds, update period

# MCSS Settings
API_BASE_URL = "YOUR_SERVER_IP"  # https://localhost:25560 or specific ip
API_KEY = "YOUR_MCSS_API_KEY"

# IF you don't want to peint the warning message while request, uncomment the 2 lines below
#from urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
# It doesn't fix the security problem, but if you're using localhost and just get MC servers status, it's probably fine

# Settings End ---

def get_servers():
    url = f"{API_BASE_URL}/api/v2/servers"
    headers = {"apiKey": API_KEY}

    response = requests.get(url, headers=headers, verify=False)
    server_message = ""
    if response.status_code == 200:
        servers = response.json()
        for server in servers:
            # server_id = server["serverId"]
            server_name = server["name"]
            server_status = server["status"]
            # print(f"Server ID: {server_id}")
            # print(f"Server Name: {server_name}")
            if server_status == 1:
                server_status = "\U0001F7E2" + " Online"  # \U0001F7E2 is a green emoji
            else:
                server_status = "\U0001F534" + " Offline"  # \U0001F7E2 is a red emoji
            # print(f"Server Status: {server_status}")
            # print('---')
            server_message = (
                server_message
                + (f"Server Name: {server_name}\n")
                + (f"Server Status: {server_status}\n")
                + "---\n"
            )
    else:
        # print(f"Request failed with status code: {response.status_code}")
        server_message = server_message + (
            f"Request failed with status code: {response.status_code}"
        )

    return server_message


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

message_reference = None


async def send_message():
    global message_reference
    channel = client.get_channel(CHANNEL_ID)
    server_message = get_servers()

    server_message = server_message + (
        "Latest updated at: " + datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    )

    # Get the last 1 messages from the channel
    async for message in channel.history(limit=1):
        if message.author == client.user:
            # Found a message sent by the bot
            message_reference = message
            break

    # Check if there's an existing message
    if message_reference and message_reference.channel == channel:
        try:
            # Edit the existing message
            await message_reference.edit(content=server_message)
        except discord.errors.NotFound:
            # If the message was deleted, send a new one
            message_reference = await channel.send(server_message)
    else:
        # Send a new message
        message_reference = await channel.send(server_message)
    # Clear console and print server_message
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print(server_message)

    


@client.event
async def on_ready():
    print("Current Login Identity:", client.user)
    game = discord.Game(DISCORD_GAME)
    await client.change_presence(
        status=BOT_STATUS, activity=game
    )  # Change BOT_STATUS at the top
    while(True):
        # Schedule the next message
        await send_message()
        await asyncio.sleep(UPDATE_PERIOD)

client.run(BOT_TOKEN)
