import sys
sys.path.append('..')

from discord.ext import commands
from discord import Embed
from util.iss_api import get_iss_location_as_coordinates, get_amount_of_people_on_iss

class IssCommand(commands.Cog):
    def __init__(self, client):
        """
        Constructor
        :param client: Client
        """
        self.client = client

    @commands.command(name='iss')
    async def iss(self, ctx):
        """
        Get the current location of the ISS and amount of astronaut on the ISS
        :param ctx: Command context
        """
        iss_embed = Embed(title="♾️ ISS Information", description="Information about the International Space Station")

        iss_embed.add_field(name="🗺️ Location", value=", ".join(get_iss_location_as_coordinates()))
        iss_embed.add_field(name="🛰️ Astronauts", value=get_amount_of_people_on_iss())

        iss_embed.set_thumbnail(url="https://media.wired.com/photos/5d0015546874e00ab2efb677/master/pass/science_iss_iss056e201352.jpg")

        iss_embed.set_footer(text="Nexus Bot", icon_url=self.client.user.avatar_url)

        await ctx.reply(embed=iss_embed)