import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.utils.predicates import ReactionPredicate
from redbot.core.utils.menus import start_adding_reactions
import json


class CallaCalla(commands.Cog):
    def __init__(self, bot):
        self.bot: Red = bot

    @commands.command()
    @commands.guild_only()
    # async def holamundo(self, ctx: commands.Context) -> None:
        # """Create a reaction emoji to mute users"""
        # if not await self.config.guild(ctx.guild).mute_role():
        #     return await ctx.send("No mute role has been setup on this server.")
        # msg = await ctx.send("React to this message to be muted!")
        # await msg.add_reaction("?")
        # await msg.add_reaction("?")
        # self.mutes.append(msg.id)
    async def callacalla(self, ctx, member: discord.Member):

        msg = await ctx.send(f"Aceptas el reto contra {ctx.author}?")
        start_adding_reactions(msg, ReactionPredicate.YES_OR_NO_EMOJIS)

        pred = ReactionPredicate.yes_or_no(msg, member)
        await ctx.bot.wait_for("reaction_add", check=pred)
        if pred.result is True:
            await member.send("has dicho si")
        else:
            await member.send("has dicho no")
