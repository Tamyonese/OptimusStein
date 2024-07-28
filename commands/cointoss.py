import discord
import random
from utils import load_data, save_data

async def cointoss(ctx, steine: int):
    user_id = str(ctx.author.id)
    data = load_data()

    user_data = data.get(user_id, {'stones': 0})
    current_stones = user_data['stones']

    if steine <= 0:
        await ctx.send("Der Einsatz muss eine positive Zahl sein.")
        return
    if steine > current_stones:
        await ctx.send("Du hast nicht genügend Steine für diesen Einsatz.")
        return

    result = random.choice(["Gewonnen", "Verloren"])

    if result == "Gewonnen":
        user_data['stones'] += steine
        message = f"Herzlichen Glückwunsch {ctx.author.display_name}! Du hast {steine} Steine gewonnen und hast jetzt {user_data['stones']} Steine."
    else:
        user_data['stones'] -= steine / 2
        message = f"Leider verloren, {ctx.author.display_name}. Du hast {steine / 2} Steine verloren und hast jetzt {user_data['stones']} Steine."

    data[user_id] = user_data
    save_data(data)

    m_embed = discord.Embed(
        title=f"Cointoss mit {steine} Steinen Einsatz",
        description=message,
        color=0x00FFFF
    )
    await ctx.respond(embed=m_embed)