import discord
from discord.ext import commands
from discord import Embed, Game, Intents
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select

class joinListener(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        print(f"{member.name} joined" )
        joinServer = member.guild
        channel = joinServer.system_channel
        embed = Embed(title="♾️ Member Join", description=f"Welcome <@{member.id}> to **{joinServer.name}**!")
        embed.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=embed)