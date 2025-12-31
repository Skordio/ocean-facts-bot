from ocean_fact_api import get_ocean_fact
import discord, logging, sys

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='bot.log')
logger = logging.getLogger(__name__)

class OceanFactBot(discord.Client):
    # Util funcs
    def help_msg(self) -> str:
        return ("Ocean Fact Bot Commands:\n"
                "$seafact - Get a random ocean fact.\n")
    
    def unknown_command_msg(self) -> str:
        return "Unknown command. Use `$seafact` to get an ocean fact."

    # Discord API funcs
    async def on_ready(self):
        logger.info(f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if not message.content or not isinstance(message.content, str):
            return
        
        formatted_msg = message.content.lower().strip().split()
        
        if len(formatted_msg) >= 1 and formatted_msg[0].startswith('$seafact'):
            if len(formatted_msg) > 1:
                match formatted_msg[1]:
                    case 'help':
                        logger.info(f'Message from {message.author}: {message.content} - Responding with help message.')
                        await message.channel.send(self.help_msg())
                    case _:
                        logger.info(f'Message from {message.author}: {message.content} - Unknown command argument.')
                        await message.channel.send(self.unknown_command_msg())
            else:
                logger.info(f'Message from {message.author}: {message.content} - Responding with an ocean fact.')
                fact = get_ocean_fact()
                await message.channel.send(fact)
        else:
            logger.info(f'Message from {message.author}: {message.content}')

def main():
    # Intialize
    intents = discord.Intents(messages=True, guilds=True, guild_messages=True, message_content=True)
    bot = OceanFactBot(intents=intents)

    # Get token
    try:
        with open('tokens/ocean_fact_bot', 'r') as file:
            token = file.read().strip()
    except FileNotFoundError:
        logger.error("Token file not found. Please ensure 'tokens/ocean_fact_bot' exists.")
        return
    except Exception as e:
        logger.error(f"Error reading token file: {str(e)}")
        return
    
    # Error handling
    def handle_error(msg: str):
        logger.error(msg)
        sys.exit(1)

    # Run
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