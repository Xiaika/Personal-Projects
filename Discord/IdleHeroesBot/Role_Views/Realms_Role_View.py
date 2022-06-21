import nextcord
import config
import discord

def custom_id(view: str, id:int) -> str:
    """Return view with id"""
    return f'{config.BOT_NAME}:{view}:{id}'

REALMS_VIEW_NAME = 'Realms_Role_View'

class RealmsRoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_click_realm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id = int(button.custom_id.split(':')[-1])
        role = interaction.guild.get_role(role_id)
        void_role = interaction.guild.get_role(988514471859335239)
        if void_role not in interaction.user.roles:
            await interaction.user.add_roles(void_role)
        assert isinstance(role, nextcord.Role)
        for r in interaction.user.roles:
            if 'Corruption' in r.name and r.name != role.name:
                await interaction.response.send_message(f'You already have {r.name} realms gate role', ephemeral=True)
                return

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f'Your {role.name} role has been removed', ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f'You have been given the {role.name} role', ephemeral=True)

    @nextcord.ui.button(label=' 120', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION120_ROLE_ID))
    async def corruption120_button(self, button, interaction):
        await self.handle_click_realm(button, interaction)

    @nextcord.ui.button(label=' 115', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION115_ROLE_ID))
    async def corruption115_button(self, button, interaction):
        await self.handle_click_realm(button, interaction)

    @nextcord.ui.button(label=' 110', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION110_ROLE_ID))
    async def corruption110_button(self, button, interaction):
        await self.handle_click_realm(button, interaction)

    @nextcord.ui.button(label=' 105', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION105_ROLE_ID))
    async def corruption105_button(self, button, interaction):
        await self.handle_click_realm(button, interaction)

    @nextcord.ui.button(label=' 100', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION100_ROLE_ID))
    async def corruption100_button(self, button, interaction):
        await self.handle_click_realm(button, interaction)

    @nextcord.ui.button(label=' 90', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION90_ROLE_ID))
    async def corruption90_button(self, button, interaction):
        await self.handle_click_realm(button, interaction)

    @nextcord.ui.button(label=' 80', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION80_ROLE_ID))
    async def corruption80_button(self, button, interaction):
        await self.handle_click_realm(button, interaction)

    @nextcord.ui.button(label=' 70', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION70_ROLE_ID))
    async def corruption70_button(self, button, interaction):
        await self.handle_click_realm(button, interaction)

    @nextcord.ui.button(label=' 60', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION60_ROLE_ID))
    async def corruption60_button(self, button, interaction):
        await self.handle_click_realm(button, interaction)

    @nextcord.ui.button(label=' 50', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION50_ROLE_ID))
    async def corruption50_button(self, button, interaction):
        await self.handle_click_realm(button, interaction)

    @nextcord.ui.button(label=' 40', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION40_ROLE_ID))
    async def corruption40_button(self, button, interaction):
        await self.handle_click_realm(button, interaction)

    @nextcord.ui.button(label=' 30', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION30_ROLE_ID))
    async def corruption30_button(self, button, interaction):
        await self.handle_click_realm(button, interaction)

    @nextcord.ui.button(label=' 20', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION20_ROLE_ID))
    async def corruption20_button(self, button, interaction):
        await self.handle_click_realm(button, interaction)

    @nextcord.ui.button(label=' 10', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION10_ROLE_ID))
    async def corruption10_button(self, button, interaction):
        await self.handle_click_realm(button, interaction)

    @nextcord.ui.button(label=' 1', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION1_ROLE_ID))
    async def corruption1_button(self, button, interaction):
        await self.handle_click_realm(button, interaction)