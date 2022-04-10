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


class Main():

    def __init__(self):
        self.client = None
        self.cursor = None

    def register_commands(self):
        self.client.remove_command("help")

        self.client.add_cog(NextLaunchCommand(self.client))
        self.client.add_cog(NewsCommand(self.client))
        self.client.add_cog(InfoCommand(self.client))
        self.client.add_cog(MarsImageCommand(self.client))
        self.client.add_cog(HelpCommand(self.client))
        self.client.add_cog(IssCommand(self.client))
        self.client.add_cog(PictureOfTheDayCommand(self.client))
        self.client.add_cog(InviteCommand(self.client))

    def register_events(self):
        self.client.add_cog(ConnectListener(self.client))
        self.client.add_cog(CommandErrorListener(self.client))

    def connect_to_database(self):
        db_data = json.load(open('mysql.json'))
        db = mysql.connector.connect(
            host=db_data['host'],
            user=db_data['user'],
            password=db_data['password'],
            database=db_data['database'])

        self.cursor = db.cursor()

    def get_cursor(self):
        return self.cursor

    def run(self):
        sys.path.append(".")

        token = json.load(open('apikeys.json'))['discord']

        intents = discord.Intents().all()
        intents.members = True

        self.client = commands.Bot("-", intents=intents)

        self.register_commands()
        self.register_events()
        self.connect_to_database()

        self.client.run(token)


Main().run()
