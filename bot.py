from ocean_fact_api import get_ocean_fact
import discord, logging, sys

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='bot.log')
logger = logging.getLogger(__name__)

class OceanFactBot(discord.Client):
    async def on_ready(self):
        logger.info(f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if not message.content or not isinstance(message.content, str):
            return
        
        if not message.content.lower().find('ocean fact') == -1:
            logger.info(f'Message from {message.author}: {message.content} - Responding with an ocean fact.')
            fact = get_ocean_fact()
            await message.channel.send(fact)
        else:
            logger.info(f'Message from {message.author}: {message.content}')

def main():
    intents = discord.Intents(messages=True, guilds=True, guild_messages=True, message_content=True)
    bot = OceanFactBot(intents=intents)

    try:
        with open('tokens/ocean_fact_bot', 'r') as file:
            token = file.read().strip()
    except FileNotFoundError:
        logger.error("Token file not found. Please ensure 'tokens/ocean_fact_bot' exists.")
        return
    
    def handle_error(msg: str):
        logger.error(msg)
        sys.exit(1)

    try:
        bot.run(token)
    except discord.LoginFailure:
        handle_error("Invalid token. Please check the token in 'tokens/ocean_fact_bot'.")
    except discord.HTTPException as e:
        handle_error(f"HTTP Exception occurred: {str(e)}")
    except Exception as e:
        handle_error(f"Error running the bot: {str(e)}")

if __name__ == '__main__':
    main()