import discord
import requests
import time
from bs4 import BeautifulSoup
from discord.ext import commands

class news: 
	
	@commands.command()
	async def news(self, ctx, source=''):
		"""Prints news articles !news <register/hackernews> """	
		if(source == ''):
			await ctx.send('Usage is !news <register/hackernews>')
			exit(0)
		
		if(source == 'register'):
			URL = 'https://www.theregister.co.uk/security'
			# Grab and parse the html page
			HTML_DOC = requests.get(URL)
			s = BeautifulSoup(HTML_DOC.text, 'html.parser')
			# headline_row titles
			headline_row = s.find_all("div", {"class": "headline_row"})
			links = headline_row[1].find_all('a')
			for i in range(1):
				links = headline_row[i].find_all('a')
				for b in links:
					await ctx.send('https://www.theregister.co.uk%s\n' % (b.get('href')))
					time.sleep(2)					
		if(source == 'hackernews'):
			URL = 'https://thehackernews.com'
		# Grab and parse the html page
			HTML_DOC = requests.get(URL)
			s = BeautifulSoup(HTML_DOC.text, 'html.parser')
		# story_link titles
			story_link = s.find_all("a", {"class": "story-link"})
			for i in range(0, 4):
				await ctx.send(story_link[i].get('href'))
				time.sleep(2)
def setup(bot):
	bot.add_cog(news())
