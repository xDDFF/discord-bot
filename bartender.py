import discord
from discord.ext import commands

TOKEN = 'NDYzMTI2OTA2MTMzNDEzOTAw.DhxRlw.OaPh-D_Xj0p8PT8fpk1SN131M0Q'
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
	
bot.run(TOKEN) 
