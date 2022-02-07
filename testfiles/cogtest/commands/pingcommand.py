import discord
from discord.ext import commands
from discord import Embed

class pingCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        author = ctx.message.author
        embed = Embed(title="♾️ Ping", description=f"🏓 Pong!\nHey, <@{author.id}>, my ping is {round(self.client.latency * 1000)} ms.")
        await ctx.reply(embed=embed)