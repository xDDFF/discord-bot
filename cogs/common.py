import asyncio
import discord
import time
import threading
from discord.ext import commands


class common:
	@commands.command()
	async def beer(self, ctx, target=''):
		'''Passes !beer <USER> a nice cold beer!'''
		if(target == ''):
			nick = ctx.author.name
		if(target != ''):
			nick = target
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
		await ctx.send('ATTENTION! GET YOUR WEED! GRIND YOUR WEED! GET READY FOR A CHANNEL-WIDE TOKE OUT!!!')
		time.sleep(10)
		for i in reversed(range(6)):
			await ctx.send('0x000'+ str(i))
			time.sleep(1)
		await ctx.send('TIME IS UP! FIRE UP YOUR BOWLS!')
	
	#; commands that need to be ported
	@commands.command()
	async def ddos(self, ctx, target=''):
		'''DDoS command, OMG DdAs cUm1n!!!'''
		if(target == ''):
			await ctx.send('Usage: !ddos <TARGET_NICK>')
		else:
			await ctx.send('_Packeting * '+target+' * from ( 127.0.0.1 ) with flags (272) for (1200) seconds._')
			time.sleep(5)
			await ctx.send('Oh shit..' '['+target+' left '+ctx.channel.name+' Ping timeout 666 seconds.] REKT\'D')
	
def setup(bot):
	bot.add_cog(common())

