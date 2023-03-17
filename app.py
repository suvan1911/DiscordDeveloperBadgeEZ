import requests

def create_app(token):
    
    json_data = {
    'name': 'NewApp',
    'team_id': None,
    }

    response = requests.post(
        'https://discord.com/api/v9/applications',
        headers={'authorization': token},
        json=json_data
        )
    
    APP_ID = response.json()["id"]
    return APP_ID
