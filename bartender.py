import discord
import time
from discord.ext import commands

TOKEN = 'BOT_TOKEN'
BOT_PREFIX = ('!', '.')

bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
	print('__bot_ready__')
	print('BOT_USERNAME : ' + bot.user.name)
	print('BOT_USER_ID : ' + str(bot.user.id))
	print('LOGGIN ENABLED...')
	print('=-=-=-=-=-=-=-=-=-=-=-')

#@bot.event
#async def on_command_error(ctx, error):

@bot.command()
async def greet(ctx):
	await ctx.send('hello')

@bot.command()
async def pack(ctx):
	await ctx.send('Grab your weed! Grind your weed! get ready! this is going to be a channel wide tokeout in 1 minute!')
	for x in reversed(range(5)):
		await ctx.send('0x000%d' % (x))
	await ctx.send('READY! FIRE UP YOUR BOWLS!!')

bot.run(TOKEN) 
