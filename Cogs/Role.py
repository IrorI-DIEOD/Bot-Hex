from discord.ext import commands
from discord.ui import Button, View
import discord

class ButtonList(View):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @discord.ui.button(label="親密20達成", style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction: discord.Interaction, button = Button):
        uid = interaction.user.id
        member = interaction.guild.get_member(uid)
        role = discord.utils.get(interaction.guild.roles, name="親密20達成")
        if role in member.roles:
            await member.remove_roles(role)
            await interaction.response.send_message("親密20達成のロールを除去しました！", ephemeral=True)
        else:
            await member.add_roles(role)
            await interaction.response.send_message("親密20達成のロールを取得しました！", ephemeral=True)

    
    @discord.ui.button(label="親密10達成", style=discord.ButtonStyle.secondary)
    async def button_callback2(self, interaction: discord.Interaction):
        uid = interaction.user.id
        member = interaction.guild.get_member(uid)
        role = discord.utils.get(interaction.guild.roles, name="親密10達成")
        if role in member.roles:
            await member.remove_roles(role)
            await interaction.response.send_message("親密10達成のロールを除去しました！", ephemeral=True)
        else:
            await member.add_roles(role)
            await interaction.response.send_message("親密10達成のロールを取得しました！", ephemeral=True)

    @discord.ui.button(label="物書き", style=discord.ButtonStyle.secondary)
    async def button_callback2(self, interaction: discord.Interaction):
        uid = interaction.user.id
        member = interaction.guild.get_member(uid)
        role = discord.utils.get(interaction.guild.roles, name="物書き")
        if role in member.roles:
            await member.remove_roles(role)
            await interaction.response.send_message("物書きのロールを除去しました！", ephemeral=True)
        else:
            await member.add_roles(role)
            await interaction.response.send_message("物書きのロールを取得しました！", ephemeral=True)

    @discord.ui.button(label="R18", style=discord.ButtonStyle.secondary)
    async def button_callback2(self, interaction: discord.Interaction):
        uid = interaction.user.id
        member = interaction.guild.get_member(uid)
        role = discord.utils.get(interaction.guild.roles, name="R18")
        if role in member.roles:
            await member.remove_roles(role)
            await interaction.response.send_message("R18のロールを除去しました！", ephemeral=True)
        else:
            await member.add_roles(role)
            await interaction.response.send_message("R18のロールを取得しました！", ephemeral=True)

class ManageRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def role(self, ctx):
        embed = discord.Embed(title = "Role List🎲",
                            description = "篠ニコ会のロール一覧です。\nお好きなものを該当するボタンから取得できます。\n" \
                            "親密20達成\n" \
                            "親密10達成\n" \
                            "物書き\n" \
                            "R18\n")

        view = ButtonList(self.bot)
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(ManageRole(bot))