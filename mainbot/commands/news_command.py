import sys
sys.path.append("..")

from discord.ext import commands
from discord import Embed
from util.spacenews_api import get_id_of_parameter, get_latest_news


class NewsCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def news(self, ctx):
        news_data = get_latest_news()

        news_embed = Embed(title=f"♾️ {news_data[get_id_of_parameter('title')]}",
                           description=f"{news_data[get_id_of_parameter('summary')]} [Read more]({news_data[get_id_of_parameter('url')]})")
        news_embed.set_thumbnail(url=news_data[get_id_of_parameter('image')])

        news_embed.set_footer(text="Nexus Bot", icon_url=ctx.message.guild.me.avatar_url)

        await ctx.reply(embed=news_embed)

