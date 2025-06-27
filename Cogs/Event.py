from discord.ext import commands
import discord

class Event(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user.name} ({self.bot.user.id})")
        print("Bot is ready!")
        ch = self.bot.get_channel(1387324984594137259)
        if ch:
            await ch.send("Bot is ready and running!")

async def setup(bot: commands.Bot):
    await bot.add_cog(Event(bot))
    print("Event cog loaded successfully.")
    print("Bot is ready to handle events.")