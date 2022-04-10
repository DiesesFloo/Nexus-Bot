from discord.ext import commands
from discord import Embed


class HelpCommand(commands.Cog):
    def __init__(self, client):
        """
        Constructor
        :param client: Client
        """
        self.client = client

    @commands.command(name='help', aliases=['h'])
    async def help(self, ctx):
        """
        Displays all commands and their descriptions.
        :param ctx: Command context
        """
        help_embed = Embed(title="♾️ Help", description="Here's a list of commands you can use")

        help_embed.add_field(name="Space Information", value="`news`, `nextlaunch`, `iss`", inline=False)
        help_embed.add_field(name="Fun", value="`marsimage`, `pictureoftheday`", inline=False)
        help_embed.add_field(name="Bot Information", value="`help`, `info`, `invite`", inline=False)

        help_embed.set_footer(text="Nexus Bot", icon_url=self.client.user.avatar_url)

        await ctx.reply(embed=help_embed)
