import sys
sys.path.append("..")

from discord.ext import commands
from discord import Embed
from util.apod_api import get_id_of_parameter, get_apod_image

class PictureOfTheDayCommand(commands.Cog):
    def __init__(self, client):
        """
        Constructor
        :param client: Client
        """
        self.client = client

    @commands.command(name='pictureoftheday', aliases=['podt', 'apod'])
    async def pictureoftheday(self, ctx):
        """
        Command to get the astronomy picture of the day from the NASA API
        :param ctx: Command context
        """
        apod_embed = Embed(title='♾️ Picture of the Day', description='The picture of the day from NASA')

        apod_embed.set_image(url=get_apod_image()[get_id_of_parameter('url')])

        apod_embed.add_field(name=f"**{get_apod_image()[get_id_of_parameter('title')]}**", value=f"{get_apod_image()[get_id_of_parameter('explanation')]}", inline=False)
        apod_embed.add_field(name=f"**Copyright**", value=f"{get_apod_image()[get_id_of_parameter('copyright')]}", inline=True)
        apod_embed.add_field(name=f"**Link**", value=f"[Click here]({get_apod_image()[get_id_of_parameter('url')]})", inline=True)

        apod_embed.set_footer(text="Nexus Bot", icon_url=self.client.user.avatar_url)

        await ctx.reply(embed=apod_embed)

