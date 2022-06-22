import nextcord
import config
from math import ceil

# TODO: add privacy to the button

EXTRA_VIEW_NAME = 'Extra_Button_View'


def dif(a, b, length):
    temp = str()
    dif = length - abs(len(a) + len(b))
    for _ in range(dif):
        temp += ' '
    return temp


class ExtraButtonView(nextcord.ui.View):
    def __init__(self, t):
        super().__init__(timeout=None)
        self.data = t
        self.LENGTH_D = 17
        self.LENGTH_M = 22

    async def handle_click_extra(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        # Formatting code
        vortex_dif_d = dif(str(self.data[0][0]), str(self.data[1][0]), self.LENGTH_D)
        realms_dif_d = dif(str(self.data[0][1]), str(self.data[1][1]),  self.LENGTH_D)
        cores_dif_d = dif(str(self.data[0][2]), str(self.data[1][2]),  self.LENGTH_D)
        hall_dif_d = dif(str(self.data[0][3]), str(self.data[1][3]),  self.LENGTH_D)
        ark_dif_d = dif(str(self.data[0][4]), str(self.data[1][4]),  self.LENGTH_D)
        vip_dif_d = dif(str(self.data[0][5]), str(self.data[1][5]),  self.LENGTH_D)
        vortex_dif_m = dif(str(self.data[0][0] * 30), str(self.data[1][0] * 30),  self.LENGTH_M)
        realms_dif_m = dif(str(self.data[0][1] * 30), str(self.data[1][1] * 30),  self.LENGTH_M)
        cores_dif_m = dif(str(self.data[0][2] * 30), str(self.data[1][2] * 30),  self.LENGTH_M)
        hall_dif_m = dif(str(self.data[0][3] * 30), str(self.data[1][3] * 30),  self.LENGTH_M)
        ark_dif_m = dif(str(self.data[0][4] * 30), str(self.data[1][4] * 30),  self.LENGTH_M)
        vip_dif_m = dif(str(self.data[0][5] * 30), str(self.data[1][5] * 30),  self.LENGTH_M)
        totals_dif_d = dif(str(self.data[2]), str(self.data[3]), self.LENGTH_D)
        totals_dif_m = dif(str(self.data[2] * 30), str(self.data[3] * 30), self.LENGTH_M)

        await interaction.response.send_message(f'Daily Income:\n'
                       f'```ㅤㅤㅤㅤㅤCoT       Stellar\n'
                       f'        ━━━━━━━━━━━━━━━━━━━━\n'
                       f'Vortex: {self.data[0][0]}{vortex_dif_d}{self.data[1][0]}\n'
                       f'Realms: {self.data[0][1]}{realms_dif_d}{self.data[1][1]}\n'
                       f' Cores: {self.data[0][2]}{cores_dif_d}{self.data[1][2]}\n'
                       f'  Hall: {self.data[0][3]}{hall_dif_d}{self.data[1][3]}\n'
                       f'   Ark: {self.data[0][4]}{ark_dif_d}{self.data[1][4]}\n'
                       f'   VIP: {self.data[0][5]}{vip_dif_d}{self.data[1][5]}\n'
                       f'        ━━━━━━━━━━━━━━━━━━━━\n'
                       f'Totals: {self.data[2]}{totals_dif_d}{self.data[3]}```'
                       f'Monthly Income:\n'
                       f'```ㅤㅤㅤㅤㅤ CoT          Stellar\n'
                       f'        ━━━━━━━━━━━━━━━━━━━━━━━━\n'
                       f'Vortex: {self.data[0][0] * 30}{vortex_dif_m}{self.data[1][0] * 30}\n'
                       f'Realms: {self.data[0][1] * 30}{realms_dif_m}{self.data[1][1] * 30}\n'
                       f' Cores: {self.data[0][2] * 30}{cores_dif_m}{self.data[1][2] * 30}\n'
                       f'  Hall: {self.data[0][3] * 30}{hall_dif_m}{self.data[1][3] * 30}\n'
                       f'   Ark: {self.data[0][4] * 30}{ark_dif_m}{self.data[1][4] * 30}\n'
                       f'   VIP: {self.data[0][5] * 30}{vip_dif_m}{self.data[1][5] * 30}\n'
                       f'        ━━━━━━━━━━━━━━━━━━━━━━━━\n'
                       f'Totals: {self.data[2] * 30}{totals_dif_m}{self.data[3] * 30}```\n', ephemeral=True)
        return

    @nextcord.ui.button(label='Extra Info', style=nextcord.ButtonStyle.green)
    async def extra_button(self, button, interaction):
        await self.handle_click_extra(button, interaction)