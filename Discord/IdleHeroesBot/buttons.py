import nextcord.ui
from nextcord.ext import commands

import config
from config import BOT_TOKEN

intents = nextcord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('Tussi is ready!')


def custom_id(view: str, id:int) -> str:
    """Return view with id"""
    return f'{config.BOT_NAME}:{view}:{id}'

VIP_VIEW_NAME = 'VIP_Role_View'

class VIP_Role_View(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

    async def handle_click_VIP(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id = int(button.custom_id.split(':')[-1])
        role = interaction.guild.get_role(role_id)
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


    async def handle_click_chest(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id = int(button.custom_id.split(':')[-1])
        role = interaction.guild.get_role(role_id)
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


    @nextcord.ui.button(label='VIP 0-1', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VIP_VIEW_NAME, config.VIP01_ROLE_ID))
    async def vip_button1(self, button, interaction):
        await self.handle_click_VIP(button, interaction)

    @nextcord.ui.button(label='VIP 2-4', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VIP_VIEW_NAME, config.VIP24_ROLE_ID))
    async def vip_button2(self, button, interaction):
        await self.handle_click_VIP(button, interaction)

    @nextcord.ui.button(label='VIP 5-6', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VIP_VIEW_NAME, config.VIP56_ROLE_ID))
    async def vip_button3(self, button, interaction):
        await self.handle_click_VIP(button, interaction)

    @nextcord.ui.button(label='VIP 7-8', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VIP_VIEW_NAME, config.VIP78_ROLE_ID))
    async def vip_button4(self, button, interaction):
        await self.handle_click_VIP(button, interaction)

    @nextcord.ui.button(label='VIP 9-10', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VIP_VIEW_NAME, config.VIP910_ROLE_ID))
    async def vip_button5(self, button, interaction):
        await self.handle_click_VIP(button, interaction)

    @nextcord.ui.button(label='VIP 11+', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VIP_VIEW_NAME, config.VIP11_ROLE_ID))
    async def vip_button6(self, button, interaction):
        await self.handle_click_VIP(button, interaction)

    @nextcord.ui.button(label='CoT Chests', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VIP_VIEW_NAME, config.CHEST_COT_ROLE_ID))
    async def cot_chest_button(self, button, interaction):
        await self.handle_click_chest(button, interaction)

    @nextcord.ui.button(label='Stellar Chests', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VIP_VIEW_NAME, config.CHEST_STELLAR_ROLE_ID))
    async def stellar_chest_button(self, button, interaction):
        await self.handle_click_chest(button, interaction)

    @nextcord.ui.button(label='No Chests', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VIP_VIEW_NAME, config.CHEST_NONE_ROLE_ID))
    async def none_chest_button(self, button, interaction):
        await self.handle_click_chest(button, interaction)



@client.command()
async def vip(ctx):
    view = VIP_Role_View()
    await ctx.send('Click a button to get a role. Click again to remove a role.'
                   '\n**__VIP Level and Chest Preferences__**', view=view)
    await view.wait()




VORTEX_VIEW_NAME = 'Vortex_Role_View'

class Vortex_Role_View(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

    async def handle_click_vortex(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id = int(button.custom_id.split(':')[-1])
        role = interaction.guild.get_role(role_id)
        assert isinstance(role, nextcord.Role)
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f'Your {role.name} role has been removed', ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f'You have been given the {role.name} role', ephemeral=True)

    @nextcord.ui.button(label='Vanquisher I', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.VANQUISHERI_ROLE_ID))
    async def vanqI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label='Vanquisher VI', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.VANQUISHERVI_ROLE_ID))
    async def vanqVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label='Defier I', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.DEFIERI_ROLE_ID))
    async def defierI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label='Defier VI', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.DEFIERVI_ROLE_ID))
    async def defierVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label='Valiant I', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.VALIANTI_ROLE_ID))
    async def valiantI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label='Valiant VI', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.VALIANTVI_ROLE_ID))
    async def valiantVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label='Explorer I', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.EXPLORERI_ROLE_ID))
    async def explorerI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label='Explorer VI', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.EXPLORERVI_ROLE_ID))
    async def explorerVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label='Pioneer I', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.PIONEERI_ROLE_ID))
    async def pioneerI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label='Pioneer VI', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.PIONEERVI_ROLE_ID))
    async def pioneerVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label='Forerunner I', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.FORERUNNERI_ROLE_ID))
    async def forerunnerI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)

    @nextcord.ui.button(label='Forerunner VI', style=nextcord.ButtonStyle.blurple,
                        custom_id=custom_id(VORTEX_VIEW_NAME, config.FORERUNNERVI_ROLE_ID))
    async def forerunnerVI_button(self, button, interaction):
        await self.handle_click_vortex(button, interaction)


@client.command()
async def vortex(ctx):
    view2 = Vortex_Role_View()
    await ctx.send('Click a button to get a role. Click again to remove a role.'
                   '\n**__Vortex Tiers__**', view=view2)
    await view2.wait()

client.run(BOT_TOKEN)