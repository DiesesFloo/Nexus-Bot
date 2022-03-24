import discord
from discord.ext import commands
from discord import Embed, Game, Intents

class nicknameCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nickname(self, ctx, *args):
        if not args:
            await ctx.reply("Mach richtig du huen")
        else:
            nickname = " ".join(args)
            await ctx.message.guild.me.edit(nick=nickname)