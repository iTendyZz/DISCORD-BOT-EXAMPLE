#Import all the important libraries for your bot
import discord as ds
from discord.ext import commands
from colorama import Fore, Back, Style
from config import TOKEN as TOKEN
import time
import platform
import random

#This construction creates your bot.
#Insert your prefix, that you wish to use with commands into command_prefix parameter.
#Intent parameter set all permissions to your bot. You can change it any time. Depends on your wish.

bot = commands.Bot(command_prefix='prefix', intents=ds.Intents.all())

#You can use @bot.event when you want to do sth when bot goes online or sth else.
#Check on_ready function description to get what it does.

@bot.event
async def on_ready():
    '''When bot is turned on it will
send your local date to console.'''
    prefix = (Back.BLACK + Fore.GREEN + time.strftime(f'%d.%m.%Y %H:%M:%S UTC', 
    time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)

    #Prints the information about system and bot's information into your console
    print(prefix + ' Logged in as ' + Fore.CYAN + bot.user.name + Fore.RESET + '')
    print(prefix + ' Bot ID ' + Fore.CYAN + str(bot.user.id) + Fore.RESET + '')
    print(prefix + ' Discord API version ' + Fore.CYAN + ds.__version__ + Fore.RESET + '')
    print(prefix + ' Python Version ' + Fore.CYAN + str(platform.python_version()) + Fore.RESET + '')
    bot.remove_command('help')


#This is your help command. It will send your text to the channel, where user used it.
#You can use all the commands in (prefix).(func_name) form in your Discord client.

@bot.command()
async def help(ctx):
    '''Insert here your hello message 
and bot will send it!'''
    await ctx.send('''TEXT''')


#Provides your bot to work online, when you insert your TOKEN into config.py file
bot.run(TOKEN)
