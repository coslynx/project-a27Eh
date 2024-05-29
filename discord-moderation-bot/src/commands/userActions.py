# userActions.py (Python)

class UserActions:
    def __init__(self, client):
        self.client = client

    async def kick_user(self, user_id, reason):
        try:
            user = await self.client.fetch_user(user_id)
            await user.kick(reason=reason)
            return True
        except Exception as e:
            print(f"Error kicking user: {e}")
            return False

    async def ban_user(self, user_id, reason):
        try:
            user = await self.client.fetch_user(user_id)
            await user.ban(reason=reason)
            return True
        except Exception as e:
            print(f"Error banning user: {e}")
            return False

    async def assign_role(self, user_id, role_id):
        try:
            user = await self.client.fetch_user(user_id)
            guild = self.client.get_guild(YOUR_GUILD_ID)
            role = guild.get_role(role_id)
            await user.add_roles(role)
            return True
        except Exception as e:
            print(f"Error assigning role: {e}")
            return False

    async def remove_role(self, user_id, role_id):
        try:
            user = await self.client.fetch_user(user_id)
            guild = self.client.get_guild(YOUR_GUILD_ID)
            role = guild.get_role(role_id)
            await user.remove_roles(role)
            return True
        except Exception as e:
            print(f"Error removing role: {e}")
            return False

    async def send_message(self, user_id, message):
        try:
            user = await self.client.fetch_user(user_id)
            await user.send(message)
            return True
        except Exception as e:
            print(f"Error sending message: {e}")
            return False

    async def report_user(self, user_id, reason):
        try:
            user = await self.client.fetch_user(user_id)
            # Implement reporting functionality here
            return True
        except Exception as e:
            print(f"Error reporting user: {e}")
            return False