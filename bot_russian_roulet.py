import discord
import time
from discord.ext import commands
from config import settings
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = settings['prefix'], intents=intents)

@bot.command(aliases = ["rulees"])
async def rules(ctx):
	await ctx.reply( f"Привет <@{ctx.author.id}>!\nЧтобы начать игру напиши /start, игра идет до первого жмурика.")

@bot.command(aliases = ["starts"])
async def start(ctx):
	await ctx.reply("И так, начинаем нашу увлекательную игру, пропишите /shot")

@bot.command(aliases = ["shoot"])
async def shot(ctx):
	x = random.randint(1, 6)
	if x == 6:
		await ctx.send( f"Оу, <@{ctx.author.id}> застрелился...")
	else:
		await ctx.send( f"<@{ctx.author.id}>, вам повезло, кто-то еще хочет испытать удачу?")








bot.run(settings['token'])
