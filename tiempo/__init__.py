from .tiempo import Tiempo

async def setup(bot):
    n = Tiempo(bot)
    await bot.add_cog(n)