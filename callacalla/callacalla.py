from re import T
import discord
import asyncio
from redbot.core import commands
from redbot.core.bot import Red
from discord.utils import get
from redbot.core.utils.predicates import ReactionPredicate
from redbot.core.utils.menus import start_adding_reactions
from random import randint

import json

class CallaCalla(commands.Cog):
    def __init__(self, bot):
        self.bot: Red = bot

    @commands.command()
    @commands.guild_only()
    async def callacalla(self, ctx, member: discord.Member):
        
        calla_embed = discord.Embed(color=0x2ecc71, title="DESAFIO CALLACALLA")
        calla_embed.add_field(name="Jugador 1:", value=f"{member.mention}", inline=True)
        calla_embed.add_field(name="vs", value="-", inline=True)
        calla_embed.add_field(name="Jugador 2:", value=f"{ctx.author.mention}", inline=True)

        sent_embed = await ctx.send(embed=calla_embed)
        
        start_adding_reactions(sent_embed, ReactionPredicate.YES_OR_NO_EMOJIS)
        
        pred = ReactionPredicate.yes_or_no(sent_embed, member)

        # await ctx.bot.wait_for("reaction_add", check=pred, timeout=30)
        await ctx.bot.wait_for("reaction_add", check=pred)
        if pred.result is True:
            value = randint(0,1)
            if value == 0:
                calla_embed.add_field(name="Ganador:", value=f"{ctx.author.mention}", inline=False)
                calla_embed.add_field(name="A chuparla:", value=f"{member.mention}", inline=False)
                perdedor = member
            else :
                calla_embed.add_field(name="Ganador:", value=f"{member.mention}", inline=False)
                calla_embed.add_field(name="A chuparla", value=f"{ctx.author.mention}", inline=False)
                perdedor = ctx.author

            await sent_embed.edit(embed=calla_embed)

            role = discord.utils.get(ctx.guild.roles, name="callacalla")

            await perdedor.add_roles(role)
            await perdedor.edit(mute=True)

            await asyncio.sleep(60)
            await perdedor.remove_roles(role)
            await perdedor.edit(mute=False)

        else:
            calla_embed.add_field(name="No ha habido juego:", value=f"{member.mention} ha sido un cobarde", inline=False)
            await sent_embed.edit(calla_embed)
