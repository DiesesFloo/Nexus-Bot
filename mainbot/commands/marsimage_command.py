import sys
sys.path.append('..')

from discord import Embed
from discord.ext import commands
from util.marsimage_api import get_random_image_from_mars_rover

class MarsImageCommand(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(name='marsimage', aliases=['mars'])
    async def marsimage(self, ctx):
        image = get_random_image_from_mars_rover()
        marsimage_embed = Embed(title="♾️ Mars Image", description="Image from [NASA's Mars Rover](https://mars.nasa.gov/rover/).\n\n")
        marsimage_embed.set_image(url=image)

        marsimage_embed.set_footer(text="Nexus Bot", icon_url=ctx.message.guild.me.avatar_url)

        await ctx.reply(embed=marsimage_embed)