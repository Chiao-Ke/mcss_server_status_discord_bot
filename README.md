# mcss_server_status_discord_bot  
A Discord bot can get your Minecraft Server Soft servers status and update it to a Discord channel.  
It's my first time write a discord bot, so there might be some problem in my code.  
I successfully run it on VSCode, and failed on Spyder.  
### So, if you use other IDE and meet some problem, please try to use VSCode.  

## Discord Bot
I didn't describe here.  
Please Google for more information.  
### And I DON'T RECOMMAND TO GIVE YOUR BOT "Administrator Permissions".
Because if your bot been hacked, your server will be cracked.  
This bot only need "Send Message" and "Manage Message" permissions.

## Installation
This code write in python.  
For convenience, I recommand you to use Anaconda or Miniconda to create an environment for it.  
Maybe you have a better way, then that's ok.  

I list my install step below:
  1.  Install Miniconda (because it's lighter than Anaconda)
  2.  Open Anaconda Prompt (You can search it in windows Start Menu)
  3.  Type `conda create --name discord python=3.10` (the `--name discord` gives your environment a name "discord") 
  4.  Then wait until environment was created
  5.  Type `conda activate discord` (activate this environment so we can install some packages we need in the right place)
  6.  Type `pip install discord.py` then enter
  7.  Type `pip install requests` then enter
  8.  Now the packages are ready
  9.  Use a code editor to open this code (I uses Visual Studio Code https://code.visualstudio.com/)
  10.  After you open the `discord_bot.py` file
  11.  You will see a part between `#Settings Starts:` and `#Settings End---`, you need to enter your own settings here
  12.  Then you can see there is a "Python Interpreter" on the right and bottom of the window, you need to Select our "discord" environment here (for more info, you caan check this https://code.visualstudio.com/docs/python/environments, or just Google it)
  13. Now, everything is done. You can start run your code by pressing "Play" buttom on the top and right of the windows (looks like a triangle)
  14. If everything is fine your code should start running

Your bot should send a message like this:  
<img width="234" alt="240317_2124587_Discord" src="https://github.com/chiao-ke/mcss_server_status_discord_bot/assets/86766885/bf7a7b37-4b3c-404c-b78c-1d17d8e6f22d">
  
Enjoy!

