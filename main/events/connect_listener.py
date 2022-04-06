from discord import Game
from discord.ext import commands


class ConnectListener(commands.Cog):
    def __init__(self, client):
        """
        Constructor
        :param client: Client
        """
        self.client = client

    @commands.Cog.listener()
    async def on_connect(self):
        """
        Called when the bot connects to Discord, set the status and print when the bot is connected
        """
        await self.client.change_presence(activity=Game(name="-help"))

        print("[ℹ️] Bot is ready")
        print(f"[ℹ️] Bot is on {len(self.client.guilds)} servers.")
