from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        if ctx.author.id != 1383504941200703539:
            pass
        await ctx.send("pong")

async def setup(bot):
    await bot.add_cog(ping(bot))