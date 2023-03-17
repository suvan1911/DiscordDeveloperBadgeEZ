import discord
from discord.ext import commands

bot = commands.Bot()

@bot.slash_command(name="first_slash", guild_ids=[1052620492969889812]) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_slash(ctx): 
    await ctx.respond("You executed the slash command!")

def run_bot(token):
    bot.run(token)

