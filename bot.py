from ocean_fact_api import get_ocean_fact
import discord

# First draft
class OceanFactBot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # Error handling for message content
        if not message.content or not isinstance(message.content, str):
            return
        # Ignore messages from the bot itself
        if message.author == self.user:
            return
        if not message.content.lower().find('ocean fact') == -1:
            fact = get_ocean_fact()
            await message.channel.send(fact)
