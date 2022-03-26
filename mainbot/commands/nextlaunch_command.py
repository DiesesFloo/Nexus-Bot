import sys
sys.path.append("..")

from discord.ext import commands
from discord import Embed


import util.rocketlaunch_api as rocketlaunch_api


class NextLaunchCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="nextlaunch", aliases=["nl"])
    async def nextlaunch(self, ctx):
        next_launch_data = rocketlaunch_api.get_next_launch()
        next_launch_embed = Embed(title="♾️ Next launch", description="Here you can find the next launch:")

        next_launch_embed.add_field(name="🏙️ **Agency**", value=next_launch_data[rocketlaunch_api.get_id_of_parameter('agency')])
        next_launch_embed.add_field(name="📃 **Type**", value=next_launch_data[rocketlaunch_api.get_id_of_parameter('type')])
        next_launch_embed.add_field(name="⚙️ **Mission**", value=next_launch_data[rocketlaunch_api.get_id_of_parameter('mission')])
        next_launch_embed.add_field(name="🚀 **Rocket**", value=next_launch_data[rocketlaunch_api.get_id_of_parameter('rocket')])
        next_launch_embed.add_field(name="📝 **Status**", value=next_launch_data[rocketlaunch_api.get_id_of_parameter('status')])
        next_launch_embed.add_field(name="📆 **Date**", value=next_launch_data[rocketlaunch_api.get_id_of_parameter('date')])

        next_launch_embed.set_thumbnail(url=next_launch_data[rocketlaunch_api.get_id_of_parameter('image')])

        next_launch_embed.set_footer(text="Nexus Bot", icon_url=ctx.message.guild.me.avatar_url)

        await ctx.reply(embed=next_launch_embed)
