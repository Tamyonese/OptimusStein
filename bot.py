import discord
from config import BOT_TOKEN, DEBUG_GUILDS
from commands.daily import daily
from commands.steine import steine
from commands.cointoss import cointoss
from commands.give import give
from commands.help import help
from commands.ranking import ranking
from commands.monty_hall import monty_hall

m_intents = discord.Intents.default()
m_intents.message_content = True
m_intents.members = True 
m_intents.presences = True

bot = discord.Bot(
    intents=m_intents,
    debug_guilds=DEBUG_GUILDS
)

@bot.event
async def on_ready():
    print(f"{bot.user} ist aktiviert")

bot.slash_command(description="Tägliche Steine")(daily)
bot.slash_command(description="Steinkonto")(steine)
bot.slash_command(description="Alles auf rot")(cointoss)
bot.slash_command(description="Gibt Steine an einen anderen Benutzer weiter")(give)
bot.slash_command(description="Hilfe zu den Commands")(help)
bot.slash_command(description="Die Rangliste aller Steinbesitzer")(ranking)
bot.slash_command(description="Monty Hall Problem")(monty_hall)

bot.run(BOT_TOKEN)
