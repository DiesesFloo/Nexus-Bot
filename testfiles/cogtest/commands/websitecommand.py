import discord
from discord.ext import commands
from discord import Embed, Game, Intents
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select

class websiteCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def website(self, ctx):
        author = ctx.message.author
        embed = Embed(title="♾️ Website", description=f"Hey <@{author.id}>, \nWe don't have a website yet, but you can check out the website of our manager Floo.")
        await ctx.reply(embed=embed, components=[
            Button(label="Website", style=5, url="http://diesesfloo.eu/", emoji="🌐")
        ])