from random import random
import discord
import asyncio  # Asegúrate de importar asyncio para las operaciones asíncronas
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
            # Se determina la probabilidad de ganar para el autor del comando
            if ctx.author.id == '402091707937849345':  
                author_wins = random() < 0.8
            else:
                author_wins = random() < 0.5

            # Se determina la probabilidad de ganar para el miembro desafiado
            if member.id == '402091707937849345':  
                member_wins = random() < 0.8
            else:
                member_wins = not author_wins  

            # Se elige al ganador basado en las probabilidades
            if author_wins:
                ganador = ctx.author
                perdedor = member
            elif member_wins:
                ganador = member
                perdedor = ctx.author
            else:
                # En caso de que ambos sean tú y ambos pierdan, elige un ganador al azar
                ganador = ctx.author if random() < 0.5 else member
                perdedor = member if ganador == ctx.author else ctx.author

            calla_embed.add_field(name="Ganador:", value=f"{ganador.mention}", inline=False)
            calla_embed.add_field(name="A chuparla:", value=f"{perdedor.mention}", inline=False)

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
