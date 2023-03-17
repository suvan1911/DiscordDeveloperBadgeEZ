import json
import webbrowser
import time 

import app
import guild
# import dbot

with open('config.json','r') as f:
    config = json.load(f)

USER_TOKEN = config.get('TOKEN')

APP_ID = app.create_app(USER_TOKEN)
print("APP CREATED")
time.sleep(2)

BOT_TOKEN = app.create_bot(USER_TOKEN,APP_ID)
print("BOT CREATED")
time.sleep(2)

GUILD_ID = guild.create_guild(USER_TOKEN)
print("GUILD CREATED")
time.sleep(2)

guild.enable_community(USER_TOKEN,GUILD_ID)
print("COMMUNITY ENABLED")
time.sleep(2)

webbrowser.open(f"https://discord.com/api/oauth2/authorize?client_id={APP_ID}&permissions=2048&scope=bot") 
# add bot to guild, requires captcha 







