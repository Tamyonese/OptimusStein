import discord

async def help(ctx):
    commands_list = {
        "/daily": "Erhalte deine tägliche Belohnung.",
        "/steine": "Zeigt dein aktuelles Steinkonto an.",
        "/cointoss [Einsatz]": "Wette eine Anzahl von Steinen auf Kopf oder Zahl.",
        "/give [Benutzer] [Anzahl]": "Gibt eine Anzahl von Steinen an einen anderen Benutzer weiter.",
        "/ranking": "Zeige die aktuelle Stein-Rangliste an."
    }

    m_embed = discord.Embed(
        title="Hilfe",
        description="Hier sind die verfügbaren Befehle:",
        color=0x00FFFF
    )

    for command, description in commands_list.items():
        m_embed.add_field(name=command, value=description, inline=False)

    await ctx.respond(embed=m_embed)