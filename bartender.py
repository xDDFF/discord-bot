import os
import datetime
import sys
from subprocess import *
try:
	import discord
	from discord.ext import commands
except ImportError:
	print('Discord.py is not installed!')
	sys.exit(0)

TOKEN = 'BOT_TOKEN'
BOT_PREFIX = ('!', '.')

bot = commands.Bot(command_prefix=BOT_PREFIX)

extensions = ["news",
		"pack"]

@bot.event
async def on_ready():
	print('\n=-=-=-=-=-=-=-=-=-=-=-')
	print('__bot_ready__')
	print('BOT_USERNAME : ' + bot.user.name)
	print('BOT_USER_ID : ' + str(bot.user.id))
	print('LOGGIN ENABLED...')
	print('=-=-=-=-=-=-=-=-=-=-=-')


## Load extensions
if __name__ == "__main__":
    for ext in extensions:
        try:
            bot.load_extension(ext)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(ext, exc))
bot.run(TOKEN) 
