# reactionRoles.py (Python)

import discord

class ReactionRoles:
    def __init__(self, client):
        self.client = client

    async def add_reaction_role(self, message_id, emoji, role_id):
        try:
            message = await self.client.get_channel(channel_id).fetch_message(message_id)
            role = discord.utils.get(message.guild.roles, id=role_id)
            await message.add_reaction(emoji)
            await self.client.reaction_roles_db.insert_reaction_role(message_id, emoji, role_id)
        except Exception as e:
            print(f"Error in adding reaction role: {e}")

    async def remove_reaction_role(self, message_id, emoji, role_id):
        try:
            message = await self.client.get_channel(channel_id).fetch_message(message_id)
            role = discord.utils.get(message.guild.roles, id=role_id)
            await message.clear_reaction(emoji)
            await self.client.reaction_roles_db.delete_reaction_role(message_id, emoji, role_id)
        except Exception as e:
            print(f"Error in removing reaction role: {e}")

    async def handle_reaction(self, payload):
        if not payload.member.bot:
            message_id = payload.message_id
            emoji = str(payload.emoji)
            role_id = await self.client.reaction_roles_db.get_role_from_reaction(message_id, emoji)
            if role_id:
                role = discord.utils.get(payload.member.guild.roles, id=role_id)
                await payload.member.add_roles(role)

    async def setup(self):
        try:
            # Logic to set up initial reaction roles from database
            pass
        except Exception as e:
            print(f"Error in setting up reaction roles: {e}")