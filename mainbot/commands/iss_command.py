import sys
sys.path.append('..')

from discord.ext import commands
from discord import Embed
from util.iss_api import get_iss_location_as_coordinates, get_amount_of_people_on_iss

class IssCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='iss')
    async def iss(self, ctx):
        iss_embed = Embed(title="♾️ ISS Information", description="Information about the International Space Station")

        iss_embed.add_field(name="🗺️ Location", value=", ".join(get_iss_location_as_coordinates()))
        iss_embed.add_field(name="🛰️ Astronauts", value=get_amount_of_people_on_iss())

        await ctx.reply(embed=iss_embed)