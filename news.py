import discord
from discord.ext import commands

class news: 
	@commands.command()
	async def news(self, ctx):
		"""Prints news articles from The Register security """	
		await ctx.send('coming soon!')

def setup(bot):
	bot.add_cog(news())
