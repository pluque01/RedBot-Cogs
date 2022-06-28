# from re import T
import discord
import asyncio
from redbot.core import Config
from redbot.core import commands
from redbot.core.bot import Red
from discord.utils import get
# from redbot.core.utils.predicates import ReactionPredicate
# from redbot.core.utils.menus import start_adding_reactions
# from random import randint

import json

defaults = {"ServerIP": None,
            "ServerPort": None,
            "Password": None}

class MinecraftPanel(commands.Cog):
    def __init__(self, bot):
        self.config = Config.get_conf(self, identifier=854245
, force_registration=True)
        self.config.register_global(**defaults)
        self.bot: Red = bot

    @commands.command()
    @checks.is_owner()
    async def setip(self, ctx, new_ip : str):
        await self.config.ServerIP.set(new_ip)
        await ctx.send("The IP of the server has been changed!")

    @commands.command()
    async def serverinfo(self, ctx):
        server_ip = await self.config.ServerIP()
        await ctx.send(f"ServerIP: {server_ip}")