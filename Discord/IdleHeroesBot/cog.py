from nextcord.ext import commands
from buttons import VIP_Role_View

class ButtonRoles(commands.Cog, name='Button Roles'):
    """Creates buttons that assign roles"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Called when the cog is loaded"""
        print('Cog loaded')
        self.bot.add_view(VIP_Role_View())

    @commands.command()
    async def roles(self, ctx):
        """Creates a new role view"""
        await ctx.send('Click a button to add or remove a role', view=VIP_Role_View())

def setup(bot):
    bot.add_cog(ButtonRoles(bot))