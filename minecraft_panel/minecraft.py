# from re import T
import discord
import requests
from redbot.core import Config
from redbot.core import commands, checks
from redbot.core.bot import Red
# from redbot.core.utils.predicates import ReactionPredicate
# from redbot.core.utils.menus import start_adding_reactions
# from random import randint


defaults = {"ServerIP": None,
            "Token": None}
pack_images = {"nomifactory" : "https://media.forgecdn.net/avatars/777/437/638120557907947036.png"}
    

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.config = Config.get_conf(self, identifier=854245, force_registration=True)
        self.config.register_global(**defaults)
        self.bot: Red = bot

    @commands.hybrid_group(name="minecraft", aliases=["mc"])
    async def minecraft(
        self,
        ctx: commands.Context,
    ) -> None:
        return
    
    @minecraft.command(name="ip")
    @discord.app_commands.describe(
        ip="La direccion IP del servidor",
    )
    @checks.is_owner()
    async def setip(
        self,
        ctx: commands.Context,
        ip : str,
    ) -> None:
        """
        Establece la direccion IP del servidor

        `new_ip` debe ser una ip valida
        """
        await self.config.ServerIP.set(ip)
        await ctx.send("La IP del servidor ha cambiado")

    @minecraft.command(name="token")
    @discord.app_commands.describe(
        token="El token para la peticion webhook",
    )
    @checks.is_owner()
    async def setToken(
        self,
        ctx: commands.Context,
        token: str,
    ) -> None:
        """
        Establece la contraseña para realizar la petición webhook

        `contraseña` debe ser la misma contraseña establecida en la configuracion webhook del servidor
        """
        await self.config.Token.set(token)
        await ctx.send("El token del webhook ha cambiado")

    @minecraft.command(name="start")
    @discord.app_commands.describe(
        server="El servidor que se quiere iniciar",
    )
    @checks.is_owner()
    async def start(
        self,
        ctx: commands.Context,
        server: str,
    ) -> None:
        """
        Envia una peticion webhook al servidor establecido para iniciar el servidor de minecraft deseado

        `server` debe ser un servidor de minecraft valido 
        """
        server_ip = await self.config.ServerIP()
        token = await self.config.Token()
        data = {"server": f"{server}"}

        url = f"https://{server_ip}:9000/hooks/launch-server?token={token}"
        response = requests.post(url, json=data, headers={'Content-type': 'application/json'})

        if response.status_code == 200:
            embed = discord.Embed(color=0x2ecc71, title="Minecraft Server")
            embed.set_thumbnail(url=pack_images[server])
            embed.add_field(name='Servidor:', value=f"{server}")
            embed.add_field(name='Estado:', value="🟢 Servidor iniciándose")
            embed.set_footer(text='Creado por Fallen')   
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Error {response.status_code}")


    @minecraft.command(name="stop")
    @discord.app_commands.describe(
        server="El servidor que se quiere detener",
    )
    @checks.is_owner()
    async def stop(
        self,
        ctx: commands.Context,
        server: str,
    ) -> None:
        """
        Envia una peticion webhook al servidor establecido para detener el servidor de minecraft deseado

        `server` debe ser un servidor de minecraft valido 
        """
        server_ip = await self.config.ServerIP()
        token = await self.config.Token()
        
        data = {"server": f"{server}"}
        url = f"https://{server_ip}:9000/hooks/stop-server?token={token}"

        response = requests.post(url, json=data, headers={'Content-type': 'application/json'})

        if response.status_code == 200:
            embed = discord.Embed(color=0x2ecc71, title="Minecraft Server")
            embed.set_thumbnail(url=pack_images[server])
            embed.add_field(name='Servidor:', value=f"{server}")
            embed.add_field(name='Estado:', value="🔴 Servidor deteniéndose")
            embed.set_footer(text='Creado por Fallen')   
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Error {response.status_code}")



    @minecraft.command(name="info")
    @checks.is_owner()
    async def info(
        self,
        ctx:commands.Context
    ) -> None:
        server_ip = await self.config.ServerIP()
        embed = discord.Embed(color=0x2ecc71, title="Minecraft Server Info")
        embed.set_thumbnail(url="https://cdn.icon-icons.com/icons2/2699/PNG/512/minecraft_logo_icon_168974.png")
        embed.add_field(name='Server IP:', value=f"{server_ip}")
        embed.add_field(name='Port:', value='25565')
        embed.set_footer(text='Creado por Fallen')   
        await ctx.send(embed=embed)