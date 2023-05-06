from .callacalla import CallaCalla

async def setup(bot):
    n = CallaCalla(bot)
    await bot.add_cog(n)