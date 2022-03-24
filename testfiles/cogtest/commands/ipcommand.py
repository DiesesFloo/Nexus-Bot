import discord
from discord.ext import commands
from discord import Embed, Game, Intents
from random import randrange

class ipCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ip(self, ctx, member:discord.Member = None):
        author = ctx.message.author

        if member == None:
            noMemberEmbed = Embed(title="♾️ IP Command", description=f"Hey <@{author.id}>, you need to define the member you want to get the IP of.")
            await ctx.reply(embed=noMemberEmbed)
        else:
            id = member.id
            randomip = str(randrange(1, 300)) + "." + str(randrange(1, 300)) + "." + str(randrange(1, 300)) + "." + str(randrange(1, 300))
            ipEmbed = Embed(title="♾️ IP Command", description=f"The IP of <@{id}> is {randomip}")
            await ctx.reply(embed=ipEmbed)
            