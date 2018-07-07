import asyncio
import os
from os import listdir
from os.path import isfile, join

import datetime
import sys
from subprocess import *
try:
	import discord
	from discord.ext import commands
except ImportError:
	print('Discord.py is not installed!')
	sys.exit(0)

TOKEN = 'NDYzMTI2OTA2MTMzNDEzOTAw.DiAwMw.Cj4FBYtAv8tyMRJM6yDuZepKPpc'
BOT_PREFIX = ('!', '.')

bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
	print('\n=-=-=-=-=-=-=-=-=-=-=-')
	print('__bot_ready__')
	print('BOT_USERNAME : ' + bot.user.name)
	print('BOT_USER_ID : ' + str(bot.user.id))
	print('LOGGIN ENABLED...')
	print('=-=-=-=-=-=-=-=-=-=-=-')
	await load_cog()

@bot.command()
async def clear(ctx, amount=100):
	await ctx.channel.purge(limit=int(amount))

#load cogs
async def load_cog():
	for ext in [f.replace('.py', '') for f in listdir('cogs') if isfile(join('cogs', f))]:
		try:
			if not '__init__' in ext:
				print("Loading {}...".format(ext))
				bot.load_extension('cogs.' + ext)	
		except Exception as e:
            		exc = '{}: {}'.format(type(e).__name__, e)
            		print('Failed to load extension {}\n{}'.format(ext, exc))


bot.run(TOKEN) 
