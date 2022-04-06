import discord
import discord.ext.commands as commands
import sys
import json

from commands.nextlaunch_command import NextLaunchCommand
from commands.news_command import NewsCommand
from commands.info_command import InfoCommand
from commands.marsimage_command import MarsImageCommand
from commands.help_command import HelpCommand
from commands.iss_command import IssCommand
from commands.pictureoftheday_command import PictureOfTheDayCommand

from events.connect_listener import ConnectListener
from events.commanderror_listener import CommandErrorListener

token = json.load(open('apikeys.json'))['discord']

intents = discord.Intents().all()
intents.members = True

client = commands.Bot("-", intents=intents)

sys.path.append(".")

client.remove_command("help")

client.add_cog(NextLaunchCommand(client))
client.add_cog(NewsCommand(client))
client.add_cog(InfoCommand(client))
client.add_cog(MarsImageCommand(client))
client.add_cog(HelpCommand(client))
client.add_cog(IssCommand(client))
client.add_cog(PictureOfTheDayCommand(client))

client.add_cog(ConnectListener(client))
client.add_cog(CommandErrorListener(client))

client.run(token)
