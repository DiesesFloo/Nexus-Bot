from dis import dis
from email import message
import discord
import asyncio
from discord.ext import commands

client = commands.Bot("+")

@client.event
async def on_ready():
    print('Eingeloggt als {}'.format(client.user.name))
    client.loop.create_task(status_task())


async def status_task():
        while True:
            await client.change_presence(activity=discord.Game('Next Generation of Bots'))


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(title=f"{member.name} was kicked from the Server!")
    await ctx.reply(embed=embed)


@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title=f"{member.name} was banned from the Server!")
    await ctx.reply(embed=embed)


client.run("OTM5ODI5MjA2Mjk1MTQyNDAw.Yf-iJw.cuZVaLFfPsGAZZn7vgeg66SuBhA")

