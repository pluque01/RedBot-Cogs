# from re import T
import discord
import asyncio
from redbot.core import Config
from redbot.core import commands, checks
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
    async def mcsetip(self, ctx, new_ip : str):
        await self.config.ServerIP.set(new_ip)
        await ctx.send("The IP of the server has been changed!")

    @commands.command()
    @checks.is_owner()
    async def mcsetport(self, ctx, new_port : str):
        await self.config.ServerIP.set(new_port)
        await ctx.send("The port of the server has been changed!")

    @commands.command()
    @checks.is_owner()
    async def mcsetpasswd(self, ctx, new_passwd : str):
        await self.config.ServerIP.set(new_passwd)
        await ctx.send("The password of the server has been changed!")

    @commands.command()
    async def mcserverinfo(self, ctx):
        server_ip = await self.config.ServerIP()
        server_port = await self.config.ServerPort()
        embed = discord.Embed(color=0x2ecc71, title="Minecraft Server Info")
        embed.set_thumbnail(url=f"https://cdn.icon-icons.com/icons2/2699/PNG/512/minecraft_logo_icon_168974.png")
        embed.add_field(name='Server IP:', value=f"{server_ip}")
        embed.add_field(name='Port:', value=f"{server_port}")
        embed.set_footer(text='Creado por Fallen')   
        await ctx.send(embed=embed)