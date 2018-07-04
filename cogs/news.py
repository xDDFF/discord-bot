import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

class news: 
	
	@commands.command()
	async def news(self, ctx):
		"""Prints news articles from The Register security """	
		url = 'https://www.theregister.co.uk/security'
	
		# Grab and parse the html page
		html_doc = requests.get(url)
		s = BeautifulSoup(html_doc.text, 'html.parser')

		# headline_row titles
		headline_row = s.find_all("div", {"class": "headline_row"})
		links = headline_row[1].find_all('a')
		
		for i in range(1):
			links = headline_row[i].find_all('a')
			for b in links:
				await ctx.send('https://www.theregister.co.uk%s\n' % (b.get('href')))

def setup(bot):
	bot.add_cog(news())
