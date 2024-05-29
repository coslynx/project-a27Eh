# scheduler.py (Python)

import discord
import asyncio

class Scheduler:
    def __init__(self, client):
        self.client = client

    async def scheduled_message(self, channel_id, message_content, interval_in_seconds):
        channel = self.client.get_channel(channel_id)
        while True:
            await channel.send(message_content)
            await asyncio.sleep(interval_in_seconds)

    async def start_scheduler(self, channel_id, message_content, interval_in_seconds):
        await self.scheduled_message(channel_id, message_content, interval_in_seconds)

# End of scheduler.py