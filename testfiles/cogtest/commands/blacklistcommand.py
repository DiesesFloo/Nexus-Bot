import discord
from discord.ext import commands
from discord import Embed, Game, Intents

class blacklistCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def blacklist(self, ctx, *args):
        author = ctx.message.author

        wrongUseEmbed = Embed(title="♾️ Blacklist", description="Wrong command use.")
        if not args:
            await ctx.reply(embed=wrongUseEmbed)
        else:
            if len(args) > 1:
                action = args[0]
                blacklistWord = " ".join(self.removeItemFromTuple(args, 0))
                if author.guild_permissions.manage_messages:
                    if action == "add":
                        self.addBlacklistWord(blacklistWord)
                        wordAddedEmbed = Embed(title="♾️ Blacklist", description=f"The word `{blacklistWord}` was added to the blacklist.")
                        await ctx.reply(embed=wordAddedEmbed)
                    elif action == "remove":
                        if self.wordIsBlacklisted(blacklistWord):
                            self.removeBlacklistWord(blacklistWord)
                            wordRemovedEmbed = Embed(title="♾️ Blacklist", description=f"The word `{blacklistWord}` was removed from the blacklist.")
                            await ctx.reply(embed=wordRemovedEmbed)
                        else:
                            wordNotFoundEmbed = Embed(title="♾️ Blacklist", description=f"The word `{blacklistWord}` isn't in the blacklist.")
                            await ctx.reply(embed=wordNotFoundEmbed)
                else:
                    noPermEmbed = Embed(title="️♾️ Blacklist")
                    await ctx.reply(embed=noPermEmbed)
            else:
                await ctx.reply(embed=wrongUseEmbed)

    def getBlacklistWordsAsText(self):
        print ("getBlacklistWordAsText() started")
        try:
            with open('blacklist.txt', 'r') as f:
                print("File opened")
                output = f.readline()
                print("Got output")
                return output
        except:
            print("Error while getting Blacklistwords")
            return None

    def getBlacklistWordsAsList(self):
        if self.getBlacklistWordsAsText() != None:
            output = self.getBlacklistWordsAsText().split(";")
            return output
        else:
            return None

    def addBlacklistWord(self, word:str):
        if not self.wordIsBlacklisted(word):
            blacklist = list(self.getBlacklistWordsAsList())
            blacklist.append(word)
            out = ";".join(blacklist)
            self.replace_line('../blacklist.txt', 0, out)

    def replace_line(self, file_name, line_num, text):
        lines = open(file_name, 'r').readlines()
        lines[line_num] = text
        out = open(file_name, 'w')
        out.writelines(lines)
        out.close()

    def removeItemFromTuple(self, input:tuple, index:int):
        locallist = list(input)
        locallist.pop(index)
        out = tuple(locallist)
        return out

    def removeBlacklistWord(self, word:str):
        list = self.getBlacklistWordsAsList()
        if self.wordIsBlacklisted(word):
            list.pop(list.index(word))
        output = ";".join(list)
        self.replace_line(output)

    def wordIsBlacklisted(self, word:str):
        if self.getBlacklistWordsAsList() != None:
            if word in self.getBlacklistWordsAsList():
                return True
            else:
                return False
        else:
            return False

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        messageList = message.content.split(" ")
        author = message.author
        if not author.guild_permissions.manage_messages:
            for word in messageList:
                if self.wordIsBlacklisted(word.lower()):
                    await message.delete()

    @commands.Cog.listener()
    async def on_message_edit(self, before:discord.Message, after:discord.Message):
        messageList = after.content.split(" ")
        author = after.author
        if not author.guild_permissions.manage_messages:
            for word in messageList:
                if self.wordIsBlacklisted(word.lower()):
                    await after.delete()