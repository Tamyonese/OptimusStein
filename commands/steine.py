import discord
from utils import load_data

async def steine(ctx):
    user_id = str(ctx.author.id)
    data = load_data()

    user_data = data.get(user_id, {'stones': 0})

    m_embed = discord.Embed(
        title="Aktuelle Steine",
        description=f"{ctx.author.display_name}, du hast {user_data['stones']} Steine.",
        color=0x00FFFF
    )
    await ctx.respond(embed=m_embed)