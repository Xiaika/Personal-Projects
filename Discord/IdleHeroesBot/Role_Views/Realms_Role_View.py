import nextcord
import config
from Role_Views.Options_Role_View import get_role_from_name, custom_id


REALMS_VIEW_NAME = 'Realms_Role_View'

class RealmsRoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_click_realm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction, name):
        # Get the role of the button
        role = get_role_from_name(interaction, name)
        # Get the role of the divider
        void_role = get_role_from_name(interaction, config.BOT_DIVIDER_ROLE[0])
        assert isinstance(void_role, nextcord.Role)
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
        await self.handle_click_realm(button, interaction, config.CORRUPTION120_ROLE[0])

    @nextcord.ui.button(label=' 115', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION115_ROLE_ID))
    async def corruption115_button(self, button, interaction):
        await self.handle_click_realm(button, interaction, config.CORRUPTION115_ROLE[0])

    @nextcord.ui.button(label=' 110', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION110_ROLE_ID))
    async def corruption110_button(self, button, interaction):
        await self.handle_click_realm(button, interaction, config.CORRUPTION110_ROLE[0])

    @nextcord.ui.button(label=' 105', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION105_ROLE_ID))
    async def corruption105_button(self, button, interaction):
        await self.handle_click_realm(button, interaction, config.CORRUPTION105_ROLE[0])

    @nextcord.ui.button(label=' 100', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION100_ROLE_ID))
    async def corruption100_button(self, button, interaction):
        await self.handle_click_realm(button, interaction, config.CORRUPTION100_ROLE[0])

    @nextcord.ui.button(label=' 90', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION90_ROLE_ID))
    async def corruption90_button(self, button, interaction):
        await self.handle_click_realm(button, interaction, config.CORRUPTION90_ROLE[0])

    @nextcord.ui.button(label=' 80', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION80_ROLE_ID))
    async def corruption80_button(self, button, interaction):
        await self.handle_click_realm(button, interaction, config.CORRUPTION80_ROLE[0])

    @nextcord.ui.button(label=' 70', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION70_ROLE_ID))
    async def corruption70_button(self, button, interaction):
        await self.handle_click_realm(button, interaction, config.CORRUPTION70_ROLE[0])

    @nextcord.ui.button(label=' 60', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION60_ROLE_ID))
    async def corruption60_button(self, button, interaction):
        await self.handle_click_realm(button, interaction, config.CORRUPTION60_ROLE[0])

    @nextcord.ui.button(label=' 50', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION50_ROLE_ID))
    async def corruption50_button(self, button, interaction):
        await self.handle_click_realm(button, interaction, config.CORRUPTION50_ROLE[0])

    @nextcord.ui.button(label=' 40', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION40_ROLE_ID))
    async def corruption40_button(self, button, interaction):
        await self.handle_click_realm(button, interaction, config.CORRUPTION40_ROLE[0])

    @nextcord.ui.button(label=' 30', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION30_ROLE_ID))
    async def corruption30_button(self, button, interaction):
        await self.handle_click_realm(button, interaction, config.CORRUPTION30_ROLE[0])

    @nextcord.ui.button(label=' 20', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION20_ROLE_ID))
    async def corruption20_button(self, button, interaction):
        await self.handle_click_realm(button, interaction, config.CORRUPTION20_ROLE[0])

    @nextcord.ui.button(label=' 10', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION10_ROLE_ID))
    async def corruption10_button(self, button, interaction):
        await self.handle_click_realm(button, interaction, config.CORRUPTION10_ROLE[0])

    @nextcord.ui.button(label=' 1', emoji='<:Corruption:988839532881395803>', style=nextcord.ButtonStyle.red,
                        custom_id=custom_id(REALMS_VIEW_NAME, config.CORRUPTION1_ROLE_ID))
    async def corruption1_button(self, button, interaction):
        await self.handle_click_realm(button, interaction, config.CORRUPTION1_ROLE[0])