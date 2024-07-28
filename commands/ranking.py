import discord
from utils import load_data

async def ranking(ctx):
    data = load_data()

    if data is None:
        data = {}

    # Sortiere die Benutzer nach der Anzahl der Steine
    sorted_users = sorted(data.items(), key=lambda x: x[1].get('stones', 0), reverse=True)

    m_embed = discord.Embed(
        title="Rangliste",
        description="Rangliste Besitzer von Steinen:",
        color=0x00FFFF
    )

    for index, (user_id, user_data) in enumerate(sorted_users, start=1):
        user = ctx.guild.get_member(int(user_id))  # Korrekt synchron aufrufen
        if user:
            m_embed.add_field(name=f"{index}. {user.display_name}", value=f"{user_data['stones']} Steine", inline=False)

    await ctx.respond(embed=m_embed)
