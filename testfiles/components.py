from turtle import title
import discord
from discord import Client, Intents, Embed, Game
import discord.ext.commands as commands
from discord_slash import SlashCommand, SlashContext
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select

client = commands.Bot("-")
slash = SlashCommand(client, sync_commands=True)
DiscordComponents(client)

client.remove_command("help")

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
        Button(label="Website", style=5, url="http://diesesfloo.eu/", emoji="🌐")
    ])

@client.command()
async def ping(ctx):
    author = ctx.message.author
    embed = Embed(title="♾️ Ping", description=f"🏓 Pong!\nHey, <@{author.id}>, my ping is {round(client.latency * 1000)} ms.")
    await ctx.reply(embed=embed)

@client.command()
async def help(ctx):
    try:
        author = ctx.message.author
        embed = Embed(title="♾️ Help", description="Here you can find my commands:")
        embed.add_field(name="🌐 *Website*", value="`-website`", inline=True)
        embed.add_field(name="🏓 *Ping*", value="`-ping`", inline=True)
        await author.send(embed=embed)
    except:
        errorEmbed =Embed(title="♾️ Error", description="Sorry, but I can't send you a direct message. Make sure, that you didn't block me and look, if your DMs are disabled.")
        await ctx.reply(embed=errorEmbed)

@client.event
async def on_member_join(member:discord.Member):
    joinServer = member.server
    channel = joinServer.default_channel
    print(f"{member.display_name} joined" )
    await channel.send("Moin")

client.run("OTM5NTQ4OTk1MDE2MDk3ODAz.Yf6dMA.OCleFdRyflqchx-pgaYtofUMing")
print("Bot is online.")