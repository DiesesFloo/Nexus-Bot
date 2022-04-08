import discord
from discord.ext import commands
from discord import Embed
import requests


class InfoCommand(commands.Cog):
    def __init__(self, client):
        """
        Constructor
        :param client: Client
        """
        self.client = client

    @commands.command(name='info')
    async def info(self, ctx):
        """
        Displays information about the bot
        :param ctx: Command context
        """
        servers = len(self.client.guilds)
        latency = round(self.client.latency * 1000)
        contributors = ", ".join(self.get_contributors())

        info_embed = Embed(title="♾️ Bot Info", description="Here you can find information about the bot:")

        info_embed.add_field(name="🖥️ **Servers**", value=str(servers))
        info_embed.add_field(name="🏓 **Latency**", value=f"{latency}ms")
        info_embed.add_field(name="👾 **Contributors**", value=contributors)
        info_embed.add_field(name="😺 **GitHub**", value="[Nexus-Bot](https://github.com/diesesfloo/Nexus-Bot)")

        info_embed.set_thumbnail(url=f"{self.client.user.avatar_url}?size=1024")

        info_embed.set_footer(text="Nexus Bot", icon_url=self.client.user.avatar_url)

        await ctx.reply(embed=info_embed)

    @staticmethod
    def get_contributors():
        """
        Get the contributors of the bot by querying the GitHub API
        :return: A list of contributors
        """
        request = requests.get("https://api.github.com/repos/diesesfloo/Nexus-Bot/contributors")
        repo_data = request.json()

        output = []

        for contributor in repo_data:
            output.append(contributor["login"])

        return output


