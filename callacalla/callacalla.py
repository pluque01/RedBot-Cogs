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

        msg = await ctx.send(f"Aceptas el reto contra {ctx.author.mention}?")
        start_adding_reactions(msg, ReactionPredicate.YES_OR_NO_EMOJIS)

        pred = ReactionPredicate.yes_or_no(msg, member)
        await ctx.bot.wait_for("reaction_add", check=pred)
        if pred.result is True:
            value = randint(0,1)
            if value == 0:
                await ctx.send(f"Ha ganado {ctx.author.mention}")
                perdedor = member
            else :
                await ctx.send(f"Ha ganado {member.mention}")
                perdedor = ctx.author

            # str_perdedor = str(perdedor.id) + ' callacalla 2 minutes'
            # await ctx.send(str_perdedor)
            # await ctx.invoke(self.bot.get_command("mute"), (perdedor, ' callacalla 2 minutes'))
            role = discord.utils.get(ctx.guild.roles, name="callacalla")

            await perdedor.add_roles(role)
            await perdedor.edit(mute=True)
            await ctx.send(f"A chuparla {perdedor.mention}")

            await asyncio.sleep(60)
            await perdedor.remove_roles(role)
            await perdedor.edit(mute=False)
            await ctx.send(f"{perdedor.mention} ha vuelto a la vida")


        else:
            await ctx.send(f"{member.mention} ha sido un cobarde")
