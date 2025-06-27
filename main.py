from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
import logging

load_dotenv()  # これを追加して、.envファイルを読み込む

# Set the logging level for discord.py to DEBUG
logging.basicConfig(level=logging.DEBUG)

# token
token = os.getenv("BOT-TOKEN")

# cog list
INITIAL_EXTENSIONS = [
    'Cogs.Event',
    'Cogs.ping',
    'Cogs.Role',
]

class Hex(commands.Bot):
    def __init__(self, command_prefix, intents, help_command, strip_after_prefix):
        super().__init__(command_prefix=command_prefix,
                        intents=intents,
                        help_command=help_command,
                        strip_after_prefix=strip_after_prefix)
        self.remove_command('help')
        self.db = None

    async def setup_hook(self) -> None:

        #Cogs load Section
        for cog in INITIAL_EXTENSIONS:
            try:
                await self.load_extension(cog)
                logging.info(f"Successfully loaded extension {cog}")
                print(f"Successfully loaded extension {cog}")
            except Exception as e:
                logging.error(f"Failed to load extension {cog}: {e}")
                print(f"Failed to load extension {cog}: {e}")

        logging.info("Hex All Ready")

if __name__ == "__main__":
    intents = discord.Intents.all()
    bot = Hex(command_prefix='h!', intents=intents, help_command=None, strip_after_prefix=True)
    bot.run(token = token)