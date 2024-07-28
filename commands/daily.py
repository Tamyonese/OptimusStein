import discord
from datetime import datetime
from utils import load_data, save_data, has_claimed_daily

async def daily(ctx):
    user_id = str(ctx.author.id)
    data = load_data()

    user_data = data.get(user_id, {'stones': 0, 'last_claim': '2000-01-01'})

    if has_claimed_daily(user_data):
        message = "Du hast deine tägliche Belohnung bereits heute erhalten. Bitte versuche es morgen wieder."
    else:
        user_data['stones'] += 100
        user_data['last_claim'] = datetime.now().strftime('%Y-%m-%d')
        data[user_id] = user_data
        save_data(data)
        message = f"Du hast 100 Steine erhalten! Du hast jetzt {user_data['stones']} Steine."

    m_embed = discord.Embed(
        title="Tägliche Steine",
        description=message,
        color=0x00FFFF
    )
    await ctx.respond(embed=m_embed)