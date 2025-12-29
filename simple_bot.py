import discord
class SimpleBot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # Ignore messages from the bot itself
        if message.author == self.user:
            return
        print(f'Message from {message.author}: {message.content}')
        # Error handling for message content
        if not message.content or not isinstance(message.content, str):
            return
        if message.content.lower().find('hello') != -1:
            await message.channel.send('Hello!')


def main():
    intents = discord.Intents(messages=True, guilds=True, guild_messages=True, message_content=True)
    bot = SimpleBot(intents=intents)
    with open('tokens/simple_test_bot', 'r') as file:
        token = file.read().strip()
    
    bot.run(token)

if __name__ == '__main__':
    main()