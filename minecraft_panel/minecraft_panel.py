# from re import T
import discord
import asyncio
from redbot.core import Config
from redbot.core import commands, checks
from redbot.core.bot import Red
from discord.utils import get
import paramiko
# from redbot.core.utils.predicates import ReactionPredicate
# from redbot.core.utils.menus import start_adding_reactions
# from random import randint

import json

defaults = {"ServerIP": None,
            "ServerUser": None,
            "ServerPort": None,
            "Password": None}

    

class MinecraftPanel(commands.Cog):
    def __init__(self, bot):
        self.config = Config.get_conf(self, identifier=854245, force_registration=True)
        self.config.register_global(**defaults)
        self.bot: Red = bot

    def executeCommandSSH(server, user, command : str):
        # Connect
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.load_system_host_keys()
        client.connect(server, username=user)

        # Run a command
        stdin, stdout, stderr = client.exec_command(command)#'cd /home/mc/minecraft-server/RAD/RAD-Serverpack-1.50 && ./LaunchServer.sh')
        print(type(stdin))  # <class 'paramiko.channel.ChannelStdinFile'>
        print(type(stdout))  # <class 'paramiko.channel.ChannelFile'>
        print(type(stderr))  # <class 'paramiko.channel.ChannelStderrFile'>

        # Print output of command. Will wait for command to finish.
        print(f'STDOUT: {stdout.read().decode("utf8")}')
        print(f'STDERR: {stderr.read().decode("utf8")}')

        # Get return code from command (0 is default for success)
        print(f'Return code: {stdout.channel.recv_exit_status()}')

        # Because they are file objects, they need to be closed
        stdin.close()
        stdout.close()
        stderr.close()

        # Close the client itself
        client.close()

    @commands.command()
    @checks.is_owner()
    async def mcsetip(self, ctx, new_ip : str):
        await self.config.ServerIP.set(new_ip)
        await ctx.send("The IP of the server has been changed!")

    @commands.command()
    @checks.is_owner()
    async def mcsetport(self, ctx, new_port : str):
        await self.config.ServerPort.set(new_port)
        await ctx.send("The port of the server has been changed!")

    @commands.command()
    @checks.is_owner()
    async def mcsetuser(self, ctx, new_user : str):
        await self.config.ServerUser.set(new_user)
        await ctx.send("The user of the server has been changed!")

    @commands.command()
    @checks.is_owner()
    async def mcsetpasswd(self, ctx, new_passwd : str):
        await self.config.Password.set(new_passwd)
        await ctx.send("The password of the server has been changed!")

    @commands.command()
    @checks.is_owner()
    async def mcstart(self, ctx):
        server_ip = await self.config.ServerIP()
        await MinecraftPanel.executeCommandSSH(server_ip, 'mc', 'ls /')
        await ctx.send("The server has been started!")

    @commands.command()
    async def mcserverinfo(self, ctx):
        server_ip = await self.config.ServerIP()
        server_port = await self.config.ServerPort()
        embed = discord.Embed(color=0x2ecc71, title="Minecraft Server Info")
        embed.set_thumbnail(url="https://cdn.icon-icons.com/icons2/2699/PNG/512/minecraft_logo_icon_168974.png")
        embed.add_field(name='Server IP:', value=f"{server_ip}")
        embed.add_field(name='Port:', value=f"{server_port}")
        embed.set_footer(text='Creado por Fallen')   
        await ctx.send(embed=embed)