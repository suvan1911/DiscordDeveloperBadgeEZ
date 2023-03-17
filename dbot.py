from discord.ext import commands #py-cord

def initialise_bot(guild_id,token):
    bot = commands.Bot()

    @bot.slash_command(name="first_slash", guild_ids=[guild_id])
    async def first_slash(ctx): 
        await ctx.respond("You executed the slash command!")

    @bot.event
    async def on_ready():
        print('Ready!')

    bot.run(token)
