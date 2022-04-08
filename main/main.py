import discord
import discord.ext.commands as commands
import sys
import json
import mysql.connector

from commands.nextlaunch_command import NextLaunchCommand
from commands.news_command import NewsCommand
from commands.info_command import InfoCommand
from commands.marsimage_command import MarsImageCommand
from commands.help_command import HelpCommand
from commands.iss_command import IssCommand
from commands.pictureoftheday_command import PictureOfTheDayCommand
from commands.invite_command import InviteCommand

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
client.add_cog(InviteCommand(client))

client.add_cog(ConnectListener(client))
client.add_cog(CommandErrorListener(client))


db_data = json.load(open('mysql.json'))
db = mysql.connector.connect(
    host=db_data['host'],
    user=db_data['user'],
    password=db_data['password'],
    database=db_data['database'])

cursor = db.cursor()

client.run(token)
