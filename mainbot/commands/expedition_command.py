import sys
sys.path.append('..')

from discord.ext import commands
from discord import Embed
from util.expedition_api import get_id_of_parameter, get_latest_expedition


class ExpeditionCommand(commands.Cog):
    def __init__(self, client):
        """
        Constructor
        :param client:
        """
        self.client = client

    @commands.command(name='expedition')
    async def expedition(self, ctx):
        """
        Command to get the latest expedition
        :param ctx:
        """
        expedition = get_latest_expedition()

        expedition_embed = Embed(title="♾️ Expedition", description="Here you can find information about the latest expedition")
        expedition_embed.add_field(name="📄 Name", value=expedition[get_id_of_parameter("name")])
        expedition_embed.add_field(name="📅 Date", value=expedition[get_id_of_parameter("start")])
        expedition_embed.add_field(name="📅 Date", value=expedition[get_id_of_parameter("end")])
        expedition_embed.add_field(name="📝 Status", value=expedition[get_id_of_parameter("status")])

        expedition_embed.set_thumbnail(url=expedition[get_id_of_parameter("image_url")])
        expedition_embed.set_footer(text="Nexus Bot", icon_url=ctx.message.guild.me.avatar_url)

        await ctx.reply(embed=expedition_embed)
