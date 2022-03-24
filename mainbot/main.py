import discord
import discord.ext.commands as commands
import sys

from commands.nextlaunch_command import NextLaunchCommand

from events.connect_listener import ConnectListener

intents = discord.Intents().all()
intents.members = True

client = commands.Bot("-", intents=intents)

sys.path.append(".")

client.add_cog(NextLaunchCommand(client))

client.add_cog(ConnectListener(client))

client.run("OTM5NTQ4OTk1MDE2MDk3ODAz.Yf6dMA.OCleFdRyflqchx-pgaYtofUMing")