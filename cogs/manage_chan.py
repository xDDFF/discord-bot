import discord
from discord.ext import commands

class manage_chan:

		@commands.command()
		async def delete(self, ctx):
			'''Delete all messges from a channel'''
			await ctx.send('coming soon')
		
def setup(bot):
	bot.add_cog(manage_chan())
