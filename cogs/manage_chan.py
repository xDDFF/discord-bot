import discord
from discord.ext import commands


class manage_chan:
	
	@commands.command()
	async def userinfo(self, ctx):
		await ctx.send('coming soon!')
	
def setup(bot):
	bot.add_cog(manage_chan())
