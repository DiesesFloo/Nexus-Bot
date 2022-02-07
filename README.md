# Nexus Bot

## Information
### About Nexus
Nexus is a brand new Discord-bot. We are trying to combine modern design and useful or funny features. The bot is developed in python and our main database service is Firebase by Google

### About this Repository
This is the main repository for our bot developers. The code of the main bot and some test files are located here. In this repository the bot token isn't shared here, just some keys of our testbots. The token of our main-bot is only owned by Floo

### Disclaimer
You are not allowed to share or copy this code and say, that it's your own code. All rights of the code reserve to the project management.

## Styleguide
### Comments
Please comment every code you write. You don't need to comment every line, but please comment essential methods or blocks of code, so that other bot developers are easily able to understand and read your code.  
Example:
```python
#Import of the essential packages
import discord
from discord import Client, Intents, Embed, Game
import discord.ext.commands as commands
from discord_components import DiscordComponents
```

### Commands
For Commands we got a multifile system, which means that every command has it's own file. This is possible with *Cogs*. Please care about our system and put every command in the commands-folder.  
  
```python
#Import of the essential packages
import discord
from discord.ext import commands
from discord import Embed, Game, Intents
```
On the top of the file you need to import the basic packages like in every file. The only important thing is to do `from discord.ext import commands`, else you are not able to use cogs.  
```python
#Create the Class
class clearCommand(commands.Cog):
    #Create the Class
    def __init__(self, client):
        self.client = client
```
Then you need to create a class. The name of the class is `commandnameCommand`. In the brackets you need to write `commands.Cog`. In the constructor you import `self` and the `client`. Then you register the constructor in `self` with `self.client = client`.
```python
#Create a command
@commands.command()
    #Create command method
    async def clear(self, ctx, amount = None):
```
Now you need to create the command with `@commands.command()`. Under this you now need create your command method. This works same like creating a normal command method, you just have to add `self` in the brackets. 
```python
#Import of the Commands
from commands.pingcommand import pingCommand
from commands.websitecommand import websiteCommand
from commands.helpcommand import helpCommand
from commands.avatarcommand import avatarCommand
from commands.ppcommand import ppCommand
from commands.clearcommand import clearCommand
from commands.announcementcommand import announcementCommand
```
After this you need import your class from your file on the top of your main.py. You can do this py writing `from commands.filename import classname`
```python
#Register command Cog-files
client.add_cog(pingCommand(client))
client.add_cog(websiteCommand(client))
client.add_cog(helpCommand(client))
client.add_cog(avatarCommand(client))
client.add_cog(ppCommand(client))
client.add_cog(clearCommand(client))
client.add_cog(announcementCommand(client))
```
At last you have to add your class as cog. You can do this by typing `client.add_cog(classname(client))`. 
