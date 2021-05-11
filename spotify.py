import requests

SPOTIFY_URL_GETTING_PLAYLIST = "	https://api.spotify.com/v1/users/dholendar1111/playlists"
ACCESS_TOKEN = "BQBMXlxQjZd3jetaud319jcW4eNnZqDnXSIbSRiGBuIXAlmoQzr_xm9pEhIlZdmF3eH0LlWn3eiixRDEyebxNwZJKF0I8tkTkFe5m6rF1MzRVPPcFnl-62fUuVemzz1qEdoqUfdjEhEGa8YqutVxCqRNi-1adeUMNw"
SPOTIFY_URL_DEVICE_ID = "https://api.spotify.com/v1/me/player/devices"


response = requests.get(
    SPOTIFY_URL_GETTING_PLAYLIST,
    headers={
        "Authorization" : f"Bearer {ACCESS_TOKEN}"
        }
    )
result = response.json()
for i in range(result['total']):
    print(result['items'][i]['name'])


def get_user_device_details():
    device_response = requests.get(
        SPOTIFY_URL_DEVICE_ID,
        headers={
            'Authorization' : f"Bearer {ACCESS_TOKEN}"
        }
    )
    device_id_response = device_response.json()
    print("{}: {}".format(device_id_response['devices'][0]['name'],device_id_response['devices'][0]['id']))
    

get_user_device_details()