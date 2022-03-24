import discord
from discord.ext import commands
from discord import Embed


class InfoCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def info(self, ctx):
        servers = len(self.client.guilds)
        latency = round(self.client.latency * 1000)
        contributors = "Floo"

        info_embed = Embed(title="♾️ Bot Info", description="Here you can find information about the bot:")

        info_embed.add_field(name="🖥️ **Servers**", value=str(servers))
        info_embed.add_field(name="🏓 **Latency**", value=f"{latency}ms")
        info_embed.add_field(name="👾 **Contributors**", value=contributors)
