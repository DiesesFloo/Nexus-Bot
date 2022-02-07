import discord
from discord.ext import commands
from discord import Embed, Game, Intents
from random import randrange

class ppCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pp(self, ctx):
        number = randrange(31)
        author = ctx.message.author
        if number == 0:
            zeroEmbed = Embed(title="♾️ PP-size", description=f"<@{author.id}> is a girl 🤡 (0cm)")
            await ctx.reply(embed=zeroEmbed)
        elif number < 14:
            smallEmbed = Embed(title="♾️ PP-size", description=f"<@{author.id}> has a small pp 🤏 ({number}cm)")
            await ctx.reply(embed=smallEmbed)
        elif number < 16:
            normalEmbed = Embed(title="♾️ PP-size", description=f"<@{author.id}> got a normal pp 🤪 ({number}cm)")
            await ctx.reply(embed=normalEmbed)
        else:
            bigEmbed = Embed(title="♾️ PP-size", description=f"<@{author.id}> has big pp 🍆 ({number}cm)")
            await ctx.reply(embed=bigEmbed)