from re import T
from textwrap import wrap
import discord
import lavalink
import requests
import urllib.parse
from redbot.core import commands
from redbot.core.bot import Red

class Lyrics(commands.Cog):
    def __init__(self, bot):
        self.bot: Red = bot

    @commands.command()
    @commands.guild_only()
    async def lyrics(self, ctx):
        try:
            player =  lavalink.get_player(ctx.guild.id)
        except:
            await ctx.send("El bot no está en ningún canal")
        else:
            try:
                query = f"{player.current.title}"
            except:
                await ctx.send("No está sonando ninguna canción :((")
            else:
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

                max_message_size = 1024 
                for i in range(0, len(lyrics), max_message_size):
                    embed.add_field(name='', value=lyrics[i:i+max_message_size], inline=False)

                embed.set_footer(text='Creado por Fallen')   
                await ctx.send(embed=embed)