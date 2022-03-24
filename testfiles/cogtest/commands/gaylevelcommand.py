from pydoc import cli
import discord
from discord.ext import commands
from discord import Embed, Game, Intents
from random import randrange

class gayLevelCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gaylevel(self, ctx, member: discord.Member = None):
        gayLevel = randrange(1, 100)
        if member == None:
            selfEmbed = Embed(title="♾️ Gay Level", description=f"🌈 You are {gayLevel}% gay 🏳️‍🌈")
            await ctx.reply(embed=selfEmbed)
        else:
            taggedId = member.id
            otherEmbed = Embed(title="♾️ Gay Level", description=f"🌈 <@{taggedId}> is {gayLevel}% gay 🏳️‍🌈")
            await ctx.reply(embed=otherEmbed)
