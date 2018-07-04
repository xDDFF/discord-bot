import discord
from discord.ext import commands

class pack:
	@commands.command()
	async def pack(self, ctx):
		"""Starts a channel wide toking countdown!!"""
		await ctx.send('we are ready to pack')

def setup(bot):
	bot.add_cog(pack())
