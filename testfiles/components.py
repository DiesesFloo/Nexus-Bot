from turtle import title
import discord
from discord import Client, Intents, Embed, Game
import discord.ext.commands as commands
from discord_slash import SlashCommand, SlashContext
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select

client = commands.Bot("-")
slash = SlashCommand(client, sync_commands=True)
DiscordComponents(client)


@client.event
async def on_connect():
    await client.change_presence(activity=discord.Game(name="Python developement"))
    print("Bot is ready.")
    print(f"Bot is on {len(client.guilds)} servers.")

@client.command()
async def website(ctx):
    author = ctx.message.author
    embed = Embed(title="♾️ Website", description=f"Hey <@{author.id}>, \nright now we don't have a website yet, but you can check out the website of our manager Floo.")
    await ctx.reply(embed=embed, components=[
        Button(label="Website", style=5, url="http://diesesfloo.eu/")
    ])

@client.command()
async def ping(ctx):
    author = ctx.message.author
    embed = Embed(title="♾️ Ping", description=f"🏓 Pong!\nHey, <@{author.id}>, my ping is {round(client.latency * 1000)} ms.")
    await ctx.reply(embed=embed)


client.run("OTM5NTQ4OTk1MDE2MDk3ODAz.Yf6dMA.OCleFdRyflqchx-pgaYtofUMing")
print("Bot is online.")