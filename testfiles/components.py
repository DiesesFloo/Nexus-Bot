from discord import Client, Intents, Embed, Game
import discord.ext.commands as commands
from discord_slash import SlashCommand, SlashContext
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select

client = commands.Bot("-")
slash = SlashCommand(client, sync_commands=True)
DiscordComponents(client)

@slash.slash(name="test", description="Just a test", guild_ids=[939533203256000532])
async def _hello(ctx:SlashContext):
    await ctx.send("Bestanden!")

@client.command()
async def hello(ctx):
    await ctx.send("hello", components= [
        [Button(label="Website", style=5,emoji="🌐", url="https://diesesfloo.eu/"),
        Button(label="Check", style=3, emoji="✅", custom_id="sucess"),
        Button(label="Uncheck", style=4, emoji="❌", custom_id="remove")]
    ])
    while True:
        interaction = await client.wait_for("button_click")
        if interaction.component.custom_id == "sucess":
            await interaction.send("✅ Du bist offiziell ein Hurensohn!")
        elif interaction.component.custom_id == "remove":
            await interaction.send("✅ Du bist nun kein Hurensohn mehr!")


client.run("OTM5NTQ4OTk1MDE2MDk3ODAz.Yf6dMA.OCleFdRyflqchx-pgaYtofUMing")
print("Bot is online.")