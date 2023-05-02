from re import T
import discord
import lavalink
import asyncio
import requests
import urllib.parse
from redbot.core import commands
from redbot.core.bot import Red

import json

class Lyrics(commands.Cog):
    def __init__(self, bot):
        self.bot: Red = bot

    @commands.command()
    @commands.guild_only()
    async def lyrics(self, ctx):
        player =  lavalink.get_player(ctx.guild.id)
        if not (player.current):
            print("No está sonando ninguna canción :((")
            return 
        else:
            query = f"{player.current.title}"
            url = "https://api.flowery.pw/v1/lyrics?query=" + urllib.parse.quote(query)

            payload={}
            headers = {
            'Accept': 'application/json',
            'User-Agent': 'Fallen-RedBot'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            song = response.json()
            lyrics = song["lyrics"]["text"]
            artwork = song["track"]["media"]["artwork"]
            
            embed = discord.Embed(color=0x2ecc71, title=f"Letra de {query}")
            embed.set_thumbnail(url=artwork)
            embed.add_field(name='', value=f"{lyrics}")
            embed.set_footer(text='Creado por Fallen')   
            await ctx.send(embed=embed)