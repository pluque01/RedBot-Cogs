from .lyrics import Lyrics 

async def setup(bot):
    n = Lyrics(bot)
    await bot.add_cog(n)