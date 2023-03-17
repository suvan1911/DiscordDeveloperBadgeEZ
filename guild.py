import requests

def create_guild(token):

    json_data = {
        'name': 'DevBadge by svn#9034',
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
        'https://discord.com/api/v9/guilds/1052620492969889812',
        headers={'authorization': token,},
        json=json_data
        )

