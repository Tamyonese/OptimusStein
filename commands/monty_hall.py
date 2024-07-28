import discord
from discord.ui import Button, View
import random

class MontyHallView(View):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.doors = ["Ziege", "Ziege", "Auto"]
        random.shuffle(self.doors)
        self.selected_door = None
        self.revealed_door = None

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        # Nur der Befehl-Aufrufer darf interagieren
        return interaction.user.id == self.user_id

    @discord.ui.button(label="Tür 1", style=discord.ButtonStyle.primary)
    async def door1(self, button: Button, interaction: discord.Interaction):
        await self.select_door(interaction, 0)

    @discord.ui.button(label="Tür 2", style=discord.ButtonStyle.primary)
    async def door2(self, button: Button, interaction: discord.Interaction):
        await self.select_door(interaction, 1)

    @discord.ui.button(label="Tür 3", style=discord.ButtonStyle.primary)
    async def door3(self, button: Button, interaction: discord.Interaction):
        await self.select_door(interaction, 2)

    async def select_door(self, interaction: discord.Interaction, door_index: int):
        self.selected_door = door_index
        # Monty wählt eine der restlichen Ziegen, die nicht die gewählte Tür ist
        remaining_doors = [i for i in range(3) if i != door_index and self.doors[i] == "Ziege"]
        self.revealed_door = random.choice(remaining_doors)

        for item in self.children:
            item.disabled = True
        self.children[self.revealed_door].label += " (Ziege)"

        await interaction.response.edit_message(content="Monty öffnet eine Tür und zeigt eine Ziege.", view=self)
        
        # Frage ob der Spieler wechseln möchte
        view = ConfirmView(self.user_id, self.doors, self.selected_door, self.revealed_door)
        await interaction.followup.send("Möchtest du die Tür wechseln?", view=view)

class ConfirmView(View):
    def __init__(self, user_id, doors, selected_door, revealed_door):
        super().__init__()
        self.user_id = user_id
        self.doors = doors
        self.selected_door = selected_door
        self.revealed_door = revealed_door

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        # Nur der Befehl-Aufrufer darf interagieren
        return interaction.user.id == self.user_id

    @discord.ui.button(label="Wechseln", style=discord.ButtonStyle.primary)
    async def switch(self, button: Button, interaction: discord.Interaction):
        # Wechseln bedeutet, die andere Tür als die gewählte und die enthüllte zu wählen
        new_selection = [i for i in range(3) if i != self.selected_door and i != self.revealed_door][0]
        await self.reveal_result(interaction, new_selection)

    @discord.ui.button(label="Behalten", style=discord.ButtonStyle.secondary)
    async def keep(self, button: Button, interaction: discord.Interaction):
        await self.reveal_result(interaction, self.selected_door)

    async def reveal_result(self, interaction: discord.Interaction, final_selection: int):
        prize = self.doors[final_selection]
        for item in self.children:
            item.disabled = True
        await interaction.response.edit_message(content=f"Du hast die Tür {'gewechselt' if final_selection != self.selected_door else 'behalten'} und {'gewonnen' if prize == 'Auto' else 'verloren'}! Hinter deiner Tür war: {prize}.", view=self)

async def monty_hall(ctx):
    view = MontyHallView(ctx.author.id)
    embed = discord.Embed(
        title="Monty Hall Problem",
        description="Wähle eine Tür und Monty wird eine andere Tür öffnen, die eine Ziege zeigt.",
        color=0x00FFFF
    )
    await ctx.respond(embed=embed, view=view)
