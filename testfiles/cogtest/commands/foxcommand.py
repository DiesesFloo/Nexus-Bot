import discord
from discord.ext import commands
from discord import Embed, Game, Intents
import requests

class foxCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fox(self, ctx):

        fox = self.getRandomFox()
        fox_embed = Embed(title="♾️ Fox", description=f"[Link here]({fox['link']})")
        fox_embed.set_image(url=fox['image'])
        await ctx.reply(embed=fox_embed)

    def getRandomFox(self):
        response = requests.get("https://randomfox.ca/floof")
        fox_data = response.json()
        return fox_data

