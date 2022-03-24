from discord import Game
from discord.ext import commands

class ConnectListener(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_connect(self):
        await self.client.change_presence(activity=Game(name="Python developement"))

        print("[ℹ️] Bot is ready")
        print(f"[ℹ️] Bot is on {len(self.client.guilds)} servers.")