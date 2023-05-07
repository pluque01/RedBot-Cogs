from .music_commands import MusicCommands

async def setup(bot):
    n = MusicCommands(bot)
    await bot.add_cog(n)