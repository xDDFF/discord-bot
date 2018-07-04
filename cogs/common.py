import discord
from discord.ext import commands

class common:
	@commands.command()
	async def beer(self, ctx):
		'''Passes !beer <USER> a nice cold beer!'''
		nick = ctx.author.name
		await ctx.send('_gives '+nick+' an ice cold WARSTEINER!_')
		await ctx.send('prost! '+nick+' enjoy!')

	@commands.command()
	async def joint(self, ctx):
		'''Lights a fat doink when needed!'''
		nick = ctx.author.name
		await ctx.send('_lights '+nick+' joint!_')
		await ctx.send('smoke that shit brah!')

	@commands.command()
	async def pack(self, ctx):
		'''Pack command ported from IRC EFNET!!!'''
	
def setup(bot):
	bot.add_cog(common())

