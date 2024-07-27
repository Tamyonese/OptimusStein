import discord
import random
from discord.commands import Option

m_intents = discord.Intents.default()
m_intents.message_content = True

bot = discord.Bot(
    intents=m_intents,
    debug_guilds=[1266747393513357382] 
)

@bot.event
async def on_ready():
    print(f"{bot.user} ist aktiviert")

@bot.slash_command(description="Alles auf rot")
async def cointoss(ctx):
    result = random.choice(["Gewonnen", "Verloren"])  
    
    m_embed = discord.Embed(
        title="Uuuund",
        description=f"Du hast {result}!",
        color=0x00FFFF
    )
    
    await ctx.respond(embed=m_embed)

@bot.event
async def on_message_delete(msg):
    await msg.channel.send(f"Ich hab das gelesen, {msg.author}")

bot.run("MTI2NjcyNzA0NjIzOTg3OTIwOA.GtdSHA.V8JTanK_xb2NL6HoSjQnb0-atXyrTtE2u1hBpk")
