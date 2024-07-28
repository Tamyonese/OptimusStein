import discord
from utils import load_data, save_data

async def give(ctx, recipient: discord.User, steine: int):
    user_id = str(ctx.author.id)
    recipient_id = str(recipient.id)
    
    data = load_data()
    
    donor_data = data.get(user_id, {'stones': 0})
    current_stones = donor_data['stones']
    recipient_data = data.get(recipient_id, {'stones': 0})

    if steine <= 0:
        await ctx.respond("Der Betrag muss eine positive Zahl sein.")
        return
    if steine > current_stones:
        await ctx.respond("Du hast nicht genügend Steine, um diese Menge zu überweisen.")
        return

    donor_data['stones'] -= steine
    recipient_data['stones'] += steine

    data[user_id] = donor_data
    data[recipient_id] = recipient_data
    save_data(data)

    m_embed = discord.Embed(
        title="Steine überwiesen",
        description=f"{ctx.author.display_name} hat {steine} Steine an {recipient.mention} überwiesen. Du hast jetzt {donor_data['stones']} Steine.\n{recipient.mention} hat jetzt {recipient_data['stones']} Steine.",
        color=0x00FFFF
    )
    await ctx.respond(embed=m_embed)