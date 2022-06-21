import nextcord
import config
import discord

def custom_id(view: str, id:int) -> str:
    """Return view with id"""
    return f'{config.BOT_NAME}:{view}:{id}'

VORTEX_VIEW_NAME = 'Vortex_Role_View'

class VortexRoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_click_vortex(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id = int(button.custom_id.split(':')[-1])
        role = interaction.guild.get_role(role_id)
        void_role = interaction.guild.get_role(988514471859335239)
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
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label=' VI', emoji='<:Vanquisher:988837947497390140>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.VANQUISHERVI_ROLE_ID))
    async def vanqVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label=' I', emoji='<:Defier:988837966497611838>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.DEFIERI_ROLE_ID))
    async def defierI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label=' VI', emoji='<:Defier:988837966497611838>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.DEFIERVI_ROLE_ID))
    async def defierVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label=' I', row=2, emoji='<:Valiant:988837980598857738>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.VALIANTI_ROLE_ID))
    async def valiantI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label=' VI', row=2, emoji='<:Valiant:988837980598857738>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.VALIANTVI_ROLE_ID))
    async def valiantVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label=' I', row=2, emoji='<:Explorer:988838004892266577>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.EXPLORERI_ROLE_ID))
    async def explorerI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label=' VI', row=2, emoji='<:Explorer:988838004892266577>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.EXPLORERVI_ROLE_ID))
    async def explorerVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label=' I', row=3, emoji='<:Pioneer:988838067693584436>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.PIONEERI_ROLE_ID))
    async def pioneerI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label=' VI', row=3, emoji='<:Pioneer:988838067693584436>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.PIONEERVI_ROLE_ID))
    async def pioneerVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label=' I', row=3, emoji='<:Forerunner:988838053915291689>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.FORERUNNERI_ROLE_ID))
    async def forerunnerI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label=' VI', row=3, emoji='<:Forerunner:988838053915291689>', style=nextcord.ButtonStyle.primary,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.FORERUNNERVI_ROLE_ID))
    async def forerunnerVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)