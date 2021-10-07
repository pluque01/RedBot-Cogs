import discord
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

        msg = await ctx.send(f"Aceptas el reto contra {ctx.author}?")
        start_adding_reactions(msg, ReactionPredicate.YES_OR_NO_EMOJIS)

        pred = ReactionPredicate.yes_or_no(msg, member)
        await ctx.bot.wait_for("reaction_add", check=pred)
        if pred.result is True:
            value = randint(0,1)
            if value == 0:
                await ctx.send(f"ha ganado {ctx.author}")
                perdedor = member
            else :
                await ctx.send(f"ha ganado {member}")
                perdedor = ctx.author
        
            await ctx.invoke(self.bot.get_command("mute"), f"{perdedor} callacalla 2 minutes")

        else:
            await ctx.send("has dicho no")
