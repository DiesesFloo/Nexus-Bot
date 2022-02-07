from turtle import title
import discord
from discord.ext import commands
from discord import Embed, Game, Intents

class clearCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, amount: int):
        author = ctx.message.author
        if author.guild_permissions.manage_messages:
            amount = amount + 1
            if(amount > 101):
                bigEmbed = Embed(title= "♾️ Clear", description=f"<@{author.id}>, I'm sorry, but I can't delete more than 100 messages.")
                await ctx.reply(embed=bigEmbed)
                return
            try:
                await ctx.channel.purge(limit=amount)

                finishEmbed = Embed(title = "♾️ Clear", description=f"Sucessfully deleted **{amount - 1}** messages.")
                await ctx.send(embed = finishEmbed)
            except:
                errorEmbed = Embed(title="♾️ Clear", desciption=f"Hey <@{author.id}>, someting went wrong 👾. Please try again.")
                ctx.reply(embed=errorEmbed)
        else:
            noPermEmbed = Embed(title = "♾️ Clear", description=f"<@{author.id}>, you are missing the permission `MANAGE_MESSAGES`.")
            await ctx.reply(embed=noPermEmbed)