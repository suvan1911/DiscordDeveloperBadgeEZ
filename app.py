import requests

def create_app(token):
    
    json_data = {
    'name': 'DevBadge by svn#9034',
    'team_id': None,
    }

    response = requests.post(
        'https://discord.com/api/v9/applications',
        headers={'authorization': token},
        json=json_data
        )
    return response.json()["id"] #application id

def create_bot(token,app_id):

    response = requests.post(
        f'https://discord.com/api/v9/applications/{app_id}/bot',
        headers={'authorization': token},
        )
    return response.json()["token"] #bot token


