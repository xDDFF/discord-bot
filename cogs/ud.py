import discord
from discord.ext import commands

class ud:
#TODO: take more than one argument as a search-term
	
	@commands.command()
	async def ud(self, ctx, search_term=''):
		if search_term == '':
			ctx.send('Usage: !ud <search_term>')
			return 0
		await ctx.send('Coming Soon!')
		url = ('https://www.urbandictionary.com/define.php?term=' + search_term)

def setup(bot):
	bot.add_cog(ud())
