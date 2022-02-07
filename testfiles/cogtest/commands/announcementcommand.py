from turtle import title
import discord
from discord.ext import commands
from discord import Embed, Game, Intents
import asyncio

class announcementCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def announcement(self, ctx, channel:discord.TextChannel = None, *, message: str = None):
        author = ctx.message.author
        if channel == None:
            noChannelEmbed = Embed(title="♾️ Announcement Command", description=f"Hey <@{author.id}>, you need to define the channel.")
            await ctx.reply(embed=noChannelEmbed)
            return
        if message == None:
            nonEmbed = Embed(title="♾️ Announcement Command", description=f"Hey <@{author.id}>, you need to define the message.")
            await ctx.reply(embed=nonEmbed)
        else:
            if author.guild_permissions.mention_everyone:
                announcementEmbed = Embed(title = "♾️ Announcement", description=message)
                await ctx.channel(embed=announcementEmbed)
                await channel.send("@everyone", delete_after=1)
            else:
                noPermEmbed = Embed(title = "♾️ Clear", description=f"<@{author.id}>, you are missing the permission `MENTION_EVERYONE`.")
                await ctx.reply(embed=noPermEmbed)