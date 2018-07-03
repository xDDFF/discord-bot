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

def check_bot_dirs():
	dirs = ("cogs", "data", "log")
	for dir in dirs:
		if not os.path.exists(dir):
			print('[%s] directory not FOUND! creating...' % (dir))
			os.makedirs(dir)

@bot.event
async def on_ready():
	print('\n=-=-=-=-=-=-=-=-=-=-=-')
	print('__bot_ready__')
	print('BOT_USERNAME : ' + bot.user.name)
	print('BOT_USER_ID : ' + str(bot.user.id))
	print('LOGGIN ENABLED...')
	print('=-=-=-=-=-=-=-=-=-=-=-')

#@bot.event
#async def on_command_error(ctx, error):

@bot.command()
async def beer(ctx):
	nick = ctx.author.display_name
	await ctx.send('_gives ' + nick + ' a cold beer!_')
	await ctx.send('is a Warsteiner! ' + nick + ' enjoy!!')

@bot.command()
async def joint(ctx):
	nick = ctx.author.display_name
	await ctx.send('_lights ' + nick + ' joint!!_')
	await ctx.send('blaze brah!!!')

check_bot_dirs()
bot.run(TOKEN) 
