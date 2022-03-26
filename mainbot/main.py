import discord
import discord.ext.commands as commands
import sys
import os

from commands.nextlaunch_command import NextLaunchCommand
from commands.news_command import NewsCommand
from commands.info_command import InfoCommand
from commands.marsimage_command import MarsImageCommand

from events.connect_listener import ConnectListener

token = ""

try:
    with open('token.txt', 'r') as f:
        token = f.readline()
except:
    print("Error while reading token.")

intents = discord.Intents().all()
intents.members = True

client = commands.Bot("-", intents=intents)

sys.path.append(".")

client.add_cog(NextLaunchCommand(client))
client.add_cog(NewsCommand(client))
client.add_cog(InfoCommand(client))
client.add_cog(MarsImageCommand(client))

client.add_cog(ConnectListener(client))

client.run(token)
