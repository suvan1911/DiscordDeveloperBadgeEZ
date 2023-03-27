from colorama import Fore, Style, init
from discord.ext import commands, Embed #py-cord
import requests
import json
import webbrowser
import time 
import os

def info():
  return f'[{Fore.YELLOW}info{Style.RESET_ALL}] »'

def suc():
  return f'[{Fore.GREEN}success{Style.RESET_ALL}] »'

def err():
  return f'[{Fore.RED}err{Style.RESET_ALL}] »'

def ext():
  input('Press enter to exit: ')
  exit()

def error_handler():

    def inner(func):

        def wrapper(*args,**kwargs):
            try:
                result = func(*args,**kwargs)
            except Exception as e:
                print(f'{err()} Could not {" ".join(func.__name__.split("_"))}.\nAdvanced log: {e}: {repr(e)}') 
                ext()
            else:
                print(f'{suc()} Successfully {func.__name__.split("_")[0]+"d " + func.__name__.split("_")[1]}')
                return result

        return wrapper

    return inner

@error_handler()           
def create_app(token):
    json_data = {
    'name': 'DevBadgeEZ by svn#9034',
    'team_id': None,
    }

    response = requests.post(
        'https://discord.com/api/v9/applications',
        headers={'authorization': token},
        json=json_data
        )
    return response.json()["id"] #application id

@error_handler()           
def create_bot(token,app_id):
    response = requests.post(
        f'https://discord.com/api/v9/applications/{app_id}/bot',
        headers={'authorization': token},
        )
    return response.json()["token"] #bot token

@error_handler()           
def create_guild(token):

    json_data = {
        'name': 'DevBadgeEZ by svn#9034',
        'icon': None,
        'channels': [],
        'system_channel_id': None,
        'guild_template_code': '2TffvPucqHkN',
    }

    response = requests.post(
        'https://discord.com/api/v9/guilds',
        headers={'authorization': token,},
        json=json_data
        )
    return response.json()["id"] #guild id 

@error_handler()           
def enable_community(token,guild_id):
    json_data = {
    'features': [
        'COMMUNITY',
    ],
    'verification_level': 1,
    'default_message_notifications': 1,
    'explicit_content_filter': 2,
    'rules_channel_id': '1',
    'public_updates_channel_id': '1',
    }

    requests.patch(
        f'https://discord.com/api/v9/guilds/{guild_id}',
        headers={'authorization': token,},
        json=json_data
        )

@error_handler()           
def initialise_bot(token):
    bot = commands.Bot()

    @bot.slash_command(name="finish")
    async def finish(ctx):
        embed=Embed(title="Success!", description="Click [here](https://discord.com/developers/active-developer) to get your badge (may take upto 24h)", color=0x00FF00)
        embed.set_author(name="svn#9034", url="https://github.com/suvan1911", icon_url="https://cdn.discordapp.com/avatars/493390106846167041/a939d325b35bb277901c96d5467dc597.webp?size=160")
        embed.set_footer(text="DevBadgeEZ by svn#9034")
        await ctx.respond(embed=embed)

    @bot.event
    async def on_ready():
        print(f"{info()} Run /finish in the newly created server.")

    bot.run(token)


if __name__ == "__main__":
    init()
    os.system("cls")

    with open('config.json','r') as f:
        config = json.load(f)

    USER_TOKEN = config.get('TOKEN')

    APP_ID = create_app(USER_TOKEN)
    time.sleep(2)

    BOT_TOKEN = create_bot(USER_TOKEN,APP_ID)
    time.sleep(2)

    GUILD_ID = create_guild(USER_TOKEN)
    time.sleep(2)

    enable_community(USER_TOKEN,GUILD_ID)
    time.sleep(2)

    print(f"{info()} Add the bot to the created server")
    webbrowser.open(f"https://discord.com/api/oauth2/authorize?client_id={APP_ID}&permissions=2048&scope=bot")
    # add bot to guild, requires captcha 

    initialise_bot(BOT_TOKEN)
    print(f"{info()} Run /finish in the newly created server to finish the process.")
    ext()

    #https://discord.com/developers/active-developer
