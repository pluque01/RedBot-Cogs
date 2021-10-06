from typing import Text
import discord
from redbot.core import commands
from redbot.core.bot import Red
import requests
import json


class Tiempo(commands.Cog):
    def __init__(self, bot):
        self.bot: Red = bot
        # self.config = Config.get_conf(
        #     self,
        #     identifier={{ cookiecutter.config_identifier }},
        #     force_registration=True,
        # )

    # async def red_delete_data_for_user(self, *, requester: RequestType, user_id: int) -> None:
    #     # TODO: Replace this with the proper end user data removal handling.
    #     super().red_delete_data_for_user(requester=requester, user_id=user_id)

    @commands.command()
    # @commands.guild_only()
    # async def holamundo(self, ctx: commands.Context) -> None:
        # """Create a reaction emoji to mute users"""
        # if not await self.config.guild(ctx.guild).mute_role():
        #     return await ctx.send("No mute role has been setup on this server.")
        # msg = await ctx.send("React to this message to be muted!")
        # await msg.add_reaction("?")
        # await msg.add_reaction("?")
        # self.mutes.append(msg.id)
    async def tiempo(self, ctx, city_name: Text):

        city_name.capitalize();

        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        openweather_key = await self.bot.get_shared_api_tokens("openweather")
        if openweather_key.get("api_key") is None:
            return await ctx.send("The Open Weather API has not ben set. Use [p]set api openweather api_key,<your-key>")
        
        # complete_url variable to store
        # complete url address
        complete_url = base_url + "appid=" + openweather_key.get("api_key") + "&q=" + city_name + "&units=metric&lang=es"
        
        # get method of requests module
        # return response object
        response = requests.get(complete_url)
        
        # json method of response object
        # convert json format data into
        # python format data
        x = response.json()
        
        # Now x contains list of nested dictionaries
        # Check the value of "cod" key is equal to
        # "404", means city is found otherwise,
        # city is not found
        if x["cod"] != "404":
        
            # store the value of "main"
            # key in variable y
            y = x["main"]
        
            # store the value corresponding
            # to the "temp" key of y
            current_temperature = y["temp"]
        
            # store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]
        
            # store the value corresponding
            # to the "humidity" key of y
            current_humidity = y["humidity"]
        
            # store the value of "weather"
            # key in variable z
            z = x["weather"]

            weather_icon = z[0]["icon"]
        
            # store the value corresponding
            # to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]

            embed = discord.Embed(color=0x2ecc71, title=f"Tiempo en {city_name}")
            embed.set_thumbnail(url=f"https://openweathermap.org/img/wn/{weather_icon}@2x.png")
            embed.add_field(name='Temperatura:', value=f"{current_temperature}°")
            embed.add_field(name='Presion atmosferica:', value=f"{current_pressure} hPa")
            embed.add_field(name='Humedad:', value=f"{current_humidity}%")
            embed.add_field(name='Descripcion:', value=weather_description)
            embed.set_footer(text='Creado por Fallen')   
            await ctx.send(embed=embed)
        
        else:
            print("No encuentro esa ciudad :(")
        