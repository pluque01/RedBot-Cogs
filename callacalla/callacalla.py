import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.utils.menus import menu, DEFAULT_CONTROLS
import json


class CallaCalla(commands.Cog):
    def __init__(self, bot):
        self.bot: Red = bot

    @commands.command()
    @commands.guild_only()
    # async def holamundo(self, ctx: commands.Context) -> None:
        # """Create a reaction emoji to mute users"""
        # if not await self.config.guild(ctx.guild).mute_role():
        #     return await ctx.send("No mute role has been setup on this server.")
        # msg = await ctx.send("React to this message to be muted!")
        # await msg.add_reaction("?")
        # await msg.add_reaction("?")
        # self.mutes.append(msg.id)
    async def callacalla(self, ctx, member: discord.Member):
        
        await member.send("Texto de prueba")
        pages = ["page 1", "page 2", "page 3"]  # or use pagify to split a long string.
        await menu(ctx, pages, DEFAULT_CONTROLS)