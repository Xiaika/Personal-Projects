import nextcord
import config
from Role_Views.Options_Role_View import get_role_from_name, custom_id


VORTEX_VIEW_NAME = 'Vortex_Role_View'

class VortexRoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_click_vortex(self, button: nextcord.ui.Button, interaction: nextcord.Interaction, name):
        # Get the role of the button
        role = get_role_from_name(interaction, name)
        # Get the role of the divider
        void_role = get_role_from_name(interaction, config.BOT_DIVIDER_ROLE[0])
        assert isinstance(void_role, nextcord.Role)
        if void_role not in interaction.user.roles:
            await interaction.user.add_roles(void_role)
        assert isinstance(role, nextcord.Role)
        for r in interaction.user.roles:
            if r.name in ['Vanquisher I', 'Vanquisher VI', 'Defier I', 'Defier VI', 'Valiant I',
                          'Valiant VI', 'Explorer I', 'Explorer VI', 'Pioneer I', 'Pioneer VI',
                          'Forerunner I', 'Forerunner VI'] and r.name != role.name:
                await interaction.response.send_message(f'You already have {r.name} vortex role', ephemeral=True)
                return
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f'Your {role.name} role has been removed', ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f'You have been given the {role.name} role', ephemeral=True)

    @nextcord.ui.button(label=' I', emoji='<:Vanquisher:988837947497390140>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.VANQUISHERI_ROLE_ID))
    async def vanqI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction, config.VANQUISHERI_ROLE[0])

    @nextcord.ui.button(label=' VI', emoji='<:Vanquisher:988837947497390140>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.VANQUISHERVI_ROLE_ID))
    async def vanqVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction, config.VANQUISHERVI_ROLE[0])

    @nextcord.ui.button(label=' I', emoji='<:Defier:988837966497611838>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.DEFIERI_ROLE_ID))
    async def defierI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction, config.DEFIERI_ROLE[0])

    @nextcord.ui.button(label=' VI', emoji='<:Defier:988837966497611838>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.DEFIERVI_ROLE_ID))
    async def defierVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction, config.DEFIERVI_ROLE[0])

    @nextcord.ui.button(label=' I', row=2, emoji='<:Valiant:988837980598857738>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.VALIANTI_ROLE_ID))
    async def valiantI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction, config.VALIANTI_ROLE[0])

    @nextcord.ui.button(label=' VI', row=2, emoji='<:Valiant:988837980598857738>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.VALIANTVI_ROLE_ID))
    async def valiantVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction, config.VALIANTVI_ROLE[0])

    @nextcord.ui.button(label=' I', row=2, emoji='<:Explorer:988838004892266577>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.EXPLORERI_ROLE_ID))
    async def explorerI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction, config.EXPLORERI_ROLE[0])

    @nextcord.ui.button(label=' VI', row=2, emoji='<:Explorer:988838004892266577>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.EXPLORERVI_ROLE_ID))
    async def explorerVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction, config.EXPLORERVI_ROLE[0])

    @nextcord.ui.button(label=' I', row=3, emoji='<:Pioneer:988838067693584436>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.PIONEERI_ROLE_ID))
    async def pioneerI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction, config.PIONEERI_ROLE[0])

    @nextcord.ui.button(label=' VI', row=3, emoji='<:Pioneer:988838067693584436>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.PIONEERVI_ROLE_ID))
    async def pioneerVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction, config.PIONEERVI_ROLE[0])

    @nextcord.ui.button(label=' I', row=3, emoji='<:Forerunner:988838053915291689>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.FORERUNNERI_ROLE_ID))
    async def forerunnerI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction, config.FORERUNNERI_ROLE[0])

    @nextcord.ui.button(label=' VI', row=3, emoji='<:Forerunner:988838053915291689>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.FORERUNNERVI_ROLE_ID))
    async def forerunnerVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction, config.FORERUNNERVI_ROLE[0])