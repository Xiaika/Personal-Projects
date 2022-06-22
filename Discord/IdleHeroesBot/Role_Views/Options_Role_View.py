import nextcord
import config

# TODO: refactor (mess with customid)
# TODO: check if user has no roles after removal and remove divider

def get_role_from_name(interaction: nextcord.Interaction, name: str):
    for r in interaction.guild.roles:
        if r.name == name:
            role = r
            break
    else:
        role = None
    return role

def custom_id(view: str, id:int) -> str:
    """Return view with id"""
    return f'{config.BOT_NAME}:{view}:{id}'

OPTIONS_VIEW_NAME = 'Options_Role_View'

class OptionsRoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_click_options(self, button: nextcord.ui.Button, interaction: nextcord.Interaction, name):
        # Get the role of the button
        role = get_role_from_name(interaction, name)
        # Get the role of the divider
        void_role = get_role_from_name(interaction, config.BOT_DIVIDER_ROLE[0])
        assert isinstance(void_role, nextcord.Role)
        if void_role not in interaction.user.roles:
            await interaction.user.add_roles(void_role)
        assert isinstance(role, nextcord.Role)
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f'Your {role.name} role has been removed', ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f'You have been given the {role.name} role', ephemeral=True)


    async def handle_click_spheres(self, button: nextcord.ui.Button, interaction: nextcord.Interaction, name):
        # Get the role of the button
        role = get_role_from_name(interaction, name)
        # Get the role of the divider
        void_role = get_role_from_name(interaction, config.BOT_DIVIDER_ROLE[0])
        if void_role not in interaction.user.roles:
            await interaction.user.add_roles(void_role)
        assert isinstance(role, nextcord.Role)
        for r in interaction.user.roles:
            if r.name in ['Sphere CoT', 'Sphere Stellar'] and r.name != role.name:
                await interaction.response.send_message(f'You already have {r.name} role', ephemeral=True)
                return
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f'Your {role.name} role has been removed', ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f'You have been given the {role.name} role', ephemeral=True)


    @nextcord.ui.button(label='Senior Card', emoji='<:Senior:988838150375886908>', style=nextcord.ButtonStyle.gray,
                        custom_id=custom_id(OPTIONS_VIEW_NAME, config.SENIOR_ROLE_ID))
    async def senior_button(self, button, interaction):
        await self.handle_click_options(button, interaction, config.SENIOR_CARD_ROLE[0])

    @nextcord.ui.button(label='BS 7', emoji='<:BrokenSpace:988837382830829670>', style=nextcord.ButtonStyle.gray,
                        custom_id=custom_id(OPTIONS_VIEW_NAME, config.BS7_ROLE_ID))
    async def bs7_button(self, button, interaction):
        await self.handle_click_options(button, interaction, config.BROKEN_SPACES_ROLE[0])

    @nextcord.ui.button(label='⟶ CoT', emoji='<:Sphere:988837355362353172>', row=2, style=nextcord.ButtonStyle.gray,
                        custom_id=custom_id(OPTIONS_VIEW_NAME, config.SPHERE_COT_ROLE_ID))
    async def sphere_cot_button(self, button, interaction):
        await self.handle_click_spheres(button, interaction, config.SPHERE_COT_ROLE[0])

    @nextcord.ui.button(label='⟶ Stellar', emoji='<:Sphere:988837355362353172>', row=2, style=nextcord.ButtonStyle.gray,
                        custom_id=custom_id(OPTIONS_VIEW_NAME, config.SPHERE_STELLAR_ROLE_ID))
    async def sphere_stellar_button(self, button, interaction):
        await self.handle_click_spheres(button, interaction, config.SPHERE_STELLAR_ROLE[0])