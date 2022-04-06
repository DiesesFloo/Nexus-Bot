from discord.ext import commands
from discord import Embed


class CommandErrorListener(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            not_found_embed = Embed(title="♾️ Error", description="This command was not found.")
            not_found_embed.set_footer(text="Nexus Bot", icon_url=self.client.user.avatar_url)
            await ctx.reply(embed=not_found_embed)
            return
        error_embed = Embed(title="♾️ Error", description=f"Error while executing command: {str(error)}.")
        error_embed.set_footer(text="Nexus Bot", icon_url=self.client.user.avatar_url)
        await ctx.reply(embed=error_embed)