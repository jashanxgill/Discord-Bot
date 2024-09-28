#installations
import random
import os
import discord
from discord.ext import commands
#variables
prefix = "!"
token = ""

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()  
    print(f'Bot {bot.user.name} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello!')

@bot.tree.command(name="hello", description="Say hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")

@bot.command(name='kick_member', description="Kick a member from the server.")
@commands.has_permissions(kick_members=True)
async def kick_member(ctx, member: discord.Member = None, *, reason=None):
    if member is None:
        await ctx.send("Please mention a user to kick. Usage: `!kick_member @user [reason]`")
        return

    if reason is None:
        reason = "No reason provided"
    
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked from the server. Reason: {reason}')

@bot.command(name='ban_member', description="Ban a member from the server.")
@commands.has_permissions(ban_members=True)
async def ban_member(ctx, member: discord.Member = None, *, reason=None):
    if member is None:
        await ctx.send("Please mention a user to ban. Usage: `!ban_member @user [reason]`")
        return

    if reason is None:
        reason = "No reason provided"

    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned from the server. Reason: {reason}')

#put your token
bot.run(token)
