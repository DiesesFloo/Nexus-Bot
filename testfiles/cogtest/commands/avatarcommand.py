import discord
from discord.ext import commands
from discord import Embed, Game, Intents

class avatarCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        author = ctx.message.author
        if(member == None):
            selfEmbed = Embed(title="♾️ Avatar", description=f"This is the avatar of <@{author.id}>:")
            selfEmbed.set_image(url=author.avatar_url)
            await ctx.reply(embed=selfEmbed)
        else:
            otherEmbed = Embed(title="♾️ Avatar", description=f"This is the avatar of <@{member.id}>:")
            otherEmbed.set_image(url=member.avatar_url)
            await ctx.reply(embed=otherEmbed)