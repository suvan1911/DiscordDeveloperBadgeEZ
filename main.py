import requests
import json
import app

with open('config.json','r') as f:
    config = json.load(f)

USER_TOKEN = config.get('TOKEN')

headers = {
    'authorization': USER_TOKEN,
}


APP_ID = app.create_app(USER_TOKEN)

response = requests.post(f'https://discord.com/api/v9/applications/{APP_ID}/bot', headers=headers)

BOT_TOKEN = response.json()["token"]
print(BOT_TOKEN)

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

response = requests.patch('https://discord.com/api/v9/guilds/1052620492969889812', headers=headers, json=json_data)



