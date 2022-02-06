import discord
import discord.ext.commands as commands

client = commands.Bot("-")

client.remove_command("help")

@client.command()
async def help(ctx):
    embed = discord.Embed(title="♾️ **Nexus Help**", description="These are the commands you can use with the bot.")
    embed.add_field(name="🤖 Test", value="`/test`", inline=False) 
    await ctx.reply(embed=embed)
    

client.run("OTM5NTQ4OTk1MDE2MDk3ODAz.Yf6dMA.OCleFdRyflqchx-pgaYtofUMing")