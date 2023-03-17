import discord
from discord.ext import commands

bot = commands.Bot()

@bot.slash_command(name="first_slash", guild_ids=[1052620492969889812])
async def first_slash(ctx): 
    await ctx.respond("You executed the slash command!")

def run_bot(token):
    bot.run(token)

