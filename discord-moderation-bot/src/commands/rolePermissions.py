# rolePermissions.py (Python)

# Import necessary libraries
import discord
from discord.ext import commands

# Create a class for RolePermissions commands
class RolePermissions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command to assign a role to a user
    @commands.command(name='assign_role', help='Assign a role to a user')
    async def assign_role(self, ctx, user: discord.Member, role: discord.Role):
        try:
            await user.add_roles(role)
            await ctx.send(f'Role {role.name} has been assigned to {user.name}')
        except Exception as e:
            await ctx.send(f'An error occurred: {e}')

    # Command to remove a role from a user
    @commands.command(name='remove_role', help='Remove a role from a user')
    async def remove_role(self, ctx, user: discord.Member, role: discord.Role):
        try:
            await user.remove_roles(role)
            await ctx.send(f'Role {role.name} has been removed from {user.name}')
        except Exception as e:
            await ctx.send(f'An error occurred: {e}')

# Setup function to add the cog to the bot
def setup(bot):
    bot.add_cog(RolePermissions(bot))