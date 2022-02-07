import discord
from discord import Client, Intents, Embed, Game
import discord.ext.commands as commands
from discord_components import DiscordComponents

#Import the Commands
from commands.pingcommand import pingCommand
from commands.websitecommand import websiteCommand
from commands.helpcommand import helpCommand
from commands.avatarcommand import avatarCommand
from commands.ppcommand import ppCommand
from commands.clearcommand import clearCommand
from commands.announcementcommand import announcementCommand

#Import the Listeners
from events.connectlistener import connectListener
from events.joinlistener import joinListener

#Set the Intents
intents = discord.Intents.all()
intents.members = True

#Register the Bot
client = commands.Bot("-",  intents=intents)
DiscordComponents(client)

#Remove Help Command (to edit it)
client.remove_command("help")

#Register command Cog-files
client.add_cog(pingCommand(client))
client.add_cog(websiteCommand(client))
client.add_cog(helpCommand(client))
client.add_cog(avatarCommand(client))
client.add_cog(ppCommand(client))
client.add_cog(clearCommand(client))
client.add_cog(announcementCommand(client))

#Register listener Cog-files
client.add_cog(connectListener(client))
client.add_cog(joinListener(client))

#Run the bot
client.run("OTM5NTQ4OTk1MDE2MDk3ODAz.Yf6dMA.OCleFdRyflqchx-pgaYtofUMing")