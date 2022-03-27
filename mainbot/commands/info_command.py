import discord
from discord.ext import commands
from discord import Embed
import requests


class InfoCommand(commands.Cog):
    def __init__(self, client):
        """
        Initialize the InfoCommand class
        :param client:
        """
        self.client = client

    @commands.command(name='info')
    async def info(self, ctx):
        """
        Displays information about the bot
        :param ctx:
        """
        servers = len(self.client.guilds)
        latency = round(self.client.latency * 1000)
        contributors = ", ".join(self.get_contributors())

        info_embed = Embed(title="♾️ Bot Info", description="Here you can find information about the bot:")

        info_embed.add_field(name="🖥️ **Servers**", value=str(servers))
        info_embed.add_field(name="🏓 **Latency**", value=f"{latency}ms")
        info_embed.add_field(name="👾 **Contributors**", value=contributors)

        info_embed.set_footer(text="Nexus Bot", icon_url=ctx.message.guild.me.avatar_url)

        await ctx.reply(embed=info_embed)

    @staticmethod
    def get_contributors():
        """
        Get the contributors of the bot by querying the GitHub API
        :return:
        """
        request = requests.get("https://api.github.com/repos/diesesfloo/Nexus-Bot/contributors")
        repo_data = request.json()

        output = []

        for contributor in repo_data:
            output.append(contributor["login"])

        return output


