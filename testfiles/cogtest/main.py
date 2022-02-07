import discord
from discord import Client, Intents, Embed, Game
import discord.ext.commands as commands
from discord_components import DiscordComponents

from commands.pingcommand import pingCommand
from commands.websitecommand import websiteCommand
from commands.helpcommand import helpCommand
from commands.avatarcommand import avatarCommand
from commands.ppcommand import ppCommand
from commands.clearcommand import clearCommand

from events.connectlistener import connectListener
from events.joinlistener import joinListener

intents = discord.Intents.all()
intents.members = True

client = commands.Bot("-",  intents=intents)
DiscordComponents(client)

client.remove_command("help")

client.add_cog(pingCommand(client))
client.add_cog(websiteCommand(client))
client.add_cog(helpCommand(client))
client.add_cog(avatarCommand(client))
client.add_cog(ppCommand(client))
client.add_cog(clearCommand(client))

client.add_cog(connectListener(client))
client.add_cog(joinListener(client))

client.run("OTM5NTQ4OTk1MDE2MDk3ODAz.Yf6dMA.OCleFdRyflqchx-pgaYtofUMing")
print("Bot is online.")