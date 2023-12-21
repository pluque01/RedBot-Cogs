from random import random
import discord
from redbot.core import commands
from discord.utils import get
from redbot.core.utils.predicates import ReactionPredicate
from redbot.core.utils.menus import start_adding_reactions

class CallaCalla(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="callacalla")
    @commands.bot_has_permissions(embed_links=True)
    @commands.guild_only()
    @discord.app_commands.describe(
        member="el miembro al que desafiar",
    )
    async def callacalla(self, ctx: commands.Context, member: discord.Member) -> None:
        """
        Desafia a un miembro del servidor a un desafio callacalla

        `member` debe ser un usuario valido y conectado a un canal de voz
        """
        calla_embed = discord.Embed(color=0x2ecc71, title="DESAFIO CALLACALLA")
        calla_embed.add_field(name="Jugador 1:", value=f"{member.mention}", inline=True)
        calla_embed.add_field(name="vs", value="-", inline=True)
        calla_embed.add_field(name="Jugador 2:", value=f"{ctx.author.mention}", inline=True)

        sent_embed = await ctx.send(embed=calla_embed)
        
        start_adding_reactions(sent_embed, ReactionPredicate.YES_OR_NO_EMOJIS)
        
        pred = ReactionPredicate.yes_or_no(sent_embed, member)

        await ctx.bot.wait_for("reaction_add", check=pred)
        
        if pred.result is True:
            # Aquí verificamos si el autor es tu usuario con una probabilidad del 80% de ganar
            if ctx.author.id == 402091707937849345:  # Reemplaza TU_ID_DE_DISCORD con tu ID de Discord real
                value = random() < 0.8
            else:
                value = random() < 0.5  # 50% de probabilidad para cualquier otro usuario

            if value:
                calla_embed.add_field(name="Ganador:", value=f"{ctx.author.mention}", inline=False)
                calla_embed.add_field(name="A chuparla:", value=f"{member.mention}", inline=False)
                perdedor = member
            else:
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
            await sent_embed.edit(embed=calla_embed)
