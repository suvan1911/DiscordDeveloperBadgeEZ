import requests

def create_guild(token):

    headers = {
        'authorization': token,
    }
    json_data = {
        'name': 'DevBadge by svn#9034',
        'icon': None,
        'channels': [],
        'system_channel_id': None,
        'guild_template_code': '2TffvPucqHkN',
    }

    requests.post('https://discord.com/api/v9/guilds', headers=headers, json=json_data)

    