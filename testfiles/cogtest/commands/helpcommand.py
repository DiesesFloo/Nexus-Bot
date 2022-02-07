import discord
from discord.ext import commands
from discord import Embed, Game, Intents

class helpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        try:
            author = ctx.message.author

            embed = Embed(title="♾️ Help", description="Here you can find my commands:")
            embed.add_field(name="🌐 **Website**", value="With `-website` you can find our website. There you are able to invite the bot to your own server.", inline=True)
            embed.add_field(name="🏓 **Ping**", value="With `-ping` you can lookup the bot-latency. There you can see, if the bot has any connection-problems.", inline=True)
            embed.add_field(name="🖼️ **Avatar**", value="With `-avatar <user>` you can get the avatar of a user. This is for example useful if you wanna download it.", inline=True)
            embed.add_field(name="🖼️ **Clear**", value="The `-clear <amount>`-command deletes the amount of messages which you enter in the first argument. To execute the command, the permission `MANAGE_MESSAGES` is required", inline=True)
            await author.send(embed=embed)

            replyEmbed = Embed(title="♾️ Help", description="Look in your DMs 😀")
            await ctx.reply(embed=replyEmbed)
        
        except:
            errorEmbed =Embed(title="♾️ Error", description="Sorry, but I can't send you a direct message. Make sure, that you didn't block me and look, if your DMs are disabled.")
            await ctx.reply(embed=errorEmbed)