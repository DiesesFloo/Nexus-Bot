import discord
from discord.ext import commands
from discord import Embed, Game, Intents

class connectListener(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_connect(self):
        await self.client.change_presence(activity=Game(name="Python developement"))
        print("Bot is ready.")
        print(f"Bot is on {len(self.client.guilds)} servers.")