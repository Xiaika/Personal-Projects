import nextcord
import config
from Role_Views.Options_Role_View import get_role_from_name, custom_id


VIP_VIEW_NAME = 'VIP_Role_View'

class VipRoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_click_VIP(self, button: nextcord.ui.Button, interaction: nextcord.Interaction, name):
        # Get the role of the button
        role = get_role_from_name(interaction, name)
        # Get the role of the divider
        void_role = get_role_from_name(interaction, config.BOT_DIVIDER_ROLE[0])
        assert isinstance(role, nextcord.Role)
        for r in interaction.user.roles:
            if 'VIP' in r.name and r.name != role.name:
                await interaction.response.send_message(f'You already have {r.name} vip role', ephemeral=True)
                return
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f'Your {role.name} role has been removed', ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f'You have been given the {role.name} role', ephemeral=True)


    async def handle_click_chest(self, button: nextcord.ui.Button, interaction: nextcord.Interaction, name):
        # Get the role of the button
        role = get_role_from_name(interaction, name)
        # Get the role of the divider
        void_role = get_role_from_name(interaction, config.BOT_DIVIDER_ROLE[0])
        assert isinstance(role, nextcord.Role)
        for r in interaction.user.roles:
            if 'Chest' in r.name and r.name != role.name:
                await interaction.response.send_message(f'You already have {r.name} chest role', ephemeral=True)
                return
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f'Your {role.name} role has been removed', ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f'You have been given the {role.name} role', ephemeral=True)


    @nextcord.ui.button(label=' 0-1', emoji='<:VIP:988836887764545596>', style=nextcord.ButtonStyle.green,
                        custom_id=custom_id(VIP_VIEW_NAME, config.VIP01_ROLE_ID))
    async def vip_button1(self, button, interaction):
        await self.handle_click_VIP(button, interaction, config.VIP0_ROLE[0])

    @nextcord.ui.button(label=' 2-4', emoji='<:VIP:988836887764545596>', style=nextcord.ButtonStyle.green,
                        custom_id=custom_id(VIP_VIEW_NAME, config.VIP24_ROLE_ID))
    async def vip_button2(self, button, interaction):
        await self.handle_click_VIP(button, interaction, config.VIP2_ROLE[0])

    @nextcord.ui.button(label=' 5-6', emoji='<:VIP:988836887764545596>', style=nextcord.ButtonStyle.green,
                        custom_id=custom_id(VIP_VIEW_NAME, config.VIP56_ROLE_ID))
    async def vip_button3(self, button, interaction):
        await self.handle_click_VIP(button, interaction, config.VIP5_ROLE[0])

    @nextcord.ui.button(label=' 7-8', emoji='<:VIP:988836887764545596>', style=nextcord.ButtonStyle.green,
                        custom_id=custom_id(VIP_VIEW_NAME, config.VIP78_ROLE_ID))
    async def vip_button4(self, button, interaction):
        await self.handle_click_VIP(button, interaction, config.VIP7_ROLE[0])

    @nextcord.ui.button(label=' 9-10', emoji='<:VIP:988836887764545596>', style=nextcord.ButtonStyle.green,
                        custom_id=custom_id(VIP_VIEW_NAME, config.VIP910_ROLE_ID))
    async def vip_button5(self, button, interaction):
        await self.handle_click_VIP(button, interaction, config.VIP9_ROLE[0])

    @nextcord.ui.button(label=' 11+', emoji='<:VIP:988836887764545596>', style=nextcord.ButtonStyle.green,
                        custom_id=custom_id(VIP_VIEW_NAME, config.VIP11_ROLE_ID))
    async def vip_button6(self, button, interaction):
        await self.handle_click_VIP(button, interaction, config.VIP11_ROLE[0])

    @nextcord.ui.button(label='  Chests', emoji='<:CoT:988837366976372767>', style=nextcord.ButtonStyle.green,
                        custom_id=custom_id(VIP_VIEW_NAME, config.CHEST_COT_ROLE_ID))
    async def cot_chest_button(self, button, interaction):
        await self.handle_click_chest(button, interaction, config.CHEST_COT_ROLE[0])

    @nextcord.ui.button(label='  Chests', emoji='<:Stellar:988837339616931914>', style=nextcord.ButtonStyle.green,
                        custom_id=custom_id(VIP_VIEW_NAME, config.CHEST_STELLAR_ROLE_ID))
    async def stellar_chest_button(self, button, interaction):
        await self.handle_click_chest(button, interaction, config.CHEST_STELLAR_ROLE[0])

    @nextcord.ui.button(label='  Chests', emoji='🚫', style=nextcord.ButtonStyle.green,
                        custom_id=custom_id(VIP_VIEW_NAME, config.CHEST_NONE_ROLE_ID))
    async def none_chest_button(self, button, interaction):
        await self.handle_click_chest(button, interaction, config.CHEST_NONE_ROLE[0])