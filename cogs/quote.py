import asyncio
import time
import threading
import os
import re
import random
import discord
from discord.ext import commands

FILE_PATH = '/home/user/discord-bot/quotes.db'

#TODO: findquote search term and print  3 results 
#TODO: put last quote as a global variable to use accross the commands.

class quotes:
	@commands.command()
	async def test(self, ctx):
		f = open(FILE_PATH, 'r')
		await ctx.send(num_lines)

	@commands.command()
	async def quote(self, ctx, quote_num=''):
		'''Display number of quotes or a specific quote by numer'''	
		f = open(FILE_PATH, 'r')
		if quote_num == '':
			num_quotes = sum(1 for line in f)
			await ctx.send('Total number of quotes on DB: '+ str(num_quotes))
			return 0
		if quote_num != '':
			for i, line in enumerate(f):
				if i == int(quote_num):
					await ctx.send('Added by: ' + f.readline()[30:-1])
		f.close()

	@commands.command()
	async def findquote(self, ctx, quote=''):
		''' Search for  a sepcific quote based on str_query'''
		if quote == '':
			await ctx.send('Usage: !quote <search_term>')
			return 0
		
		f = open(FILE_PATH, 'r')
		
		f.close()

	@commands.command()
	async def addquote(self, ctx, quote=''):
		''' Add a quote to existing quotes.db'''
		if quote == '':
			await ctx.send('Usage: !addquote <quote>')
			return 0
		#TODO: add quote number at the beggining of the quote
		t = time.localtime(time.time())	
		STAMP = ('666 %d/%d/%d %d:%d:%d #201337 %s ' % \
			(t.tm_mday, t.tm_mon,t.tm_year, t.tm_hour, t.tm_min, t.tm_sec,
			 ctx.author.name)) 
		f = open(FILE_PATH, 'a')
		await ctx.send(STAMP + quote)
		f.close()
	
	@commands.command()
	async def randquote(self, ctx, quote=''):
		''' Provide a random quote'''
		if quote != '':
			await ctx.send('Usage: !randquote <no args>')
			return 0	
		f = open(FILE_PATH, 'r')
		await ctx.send('senidng a random quote...')
		time.sleep(1)
		rand = random.randint(0,300) 
		for i, line in enumerate(f):
			if i == rand:
				await ctx.send('added by: ' + f.readline()[30:-1])
		f.close()
def setup(bot):
	bot.add_cog(quotes())
