from discord.ext import commands
from discord import Embed


class InviteCommand(commands.Cog):
    def __init__(self, client):
        """
        Constructor
        :param client: Client
        """
        self.client = client

    @commands.command(name="invite")
    async def invite(self, ctx):
        """
        Sends an Embed with the invite link
        :param ctx: Command context
        """
        invite_embed = Embed(title="♾️ Invite me to your server!",
                             description="[Click here to invite me!](https://discord.com/api/oauth2/authorize?client_id=956659875012808765&permissions=8&scope=bot%20applications.commands)")
        invite_embed.set_footer(text="Nexus Bot", icon_url=self.client.user.avatar_url)

        await ctx.reply(embed=invite_embed)
