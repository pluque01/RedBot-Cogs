from re import T
import discord
import asyncio
from redbot.core import commands, app_commands
from redbot.core.bot import Red

class MusicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: Red = bot

    @app_commands.command(name="play")
    @app_commands.guild_only()
    @app_commands.describe(
        cancion = "la cancion para reproducir",
    )
    async def play(self, ctx: commands.Context, interaction: discord.Interaction, cancion: str) -> None:
        """
        Reproduce una cancion

        `cancion` debe ser una string que corresponda a una canción
        """
        await ctx.invoke(self.bot.get_command('play'), query=cancion)
        
