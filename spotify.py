import requests

# URL'S
SPOTIFY_URL_GETTING_PLAYLIST = "https://api.spotify.com/v1/users/dholendar1111/playlists"
SPOTIFY_URL_DEVICE_ID = "https://api.spotify.com/v1/me/player/devices"
SPOTIFY_URL_PLAYING = "https://api.spotify.com/v1/me/player/play"
SPOTIFY_USER_SEARCH = "	https://api.spotify.com/v1/search"

#ACCESS TOKENS
ACCESS_TOKEN  = "BQDAmGqVxM8pAAukVuTvz61b_uFyGA6nLzxIQaw2XXRkmMANngGmNoldxu7O0PjnCwoNCZT-xNMjj8rWSXH2L0dCvGnTyIUAc2BHQ2aBr9XVmMm0j5H18cm84Uxug6s4eJPrFOse12YPPf6h9apG_AWzyethA7rM3yAhWQwQwW_t8eahyBJ5finkG2lL2S70nHPOZUxl3StKHqWnL13AEua6Bl0AYa3VLaTJsqfq4F5c1zQ5bDhvot5wi8I4Y31nqRMRTA_iG6RBhoCfgOb-JWLa90on"
device_id = []

def getting_user_playlist():
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
    print
    for i in range(len(device_id_response['devices'])):
        device_id.append(device_id_response['devices'][i]['id'])
        print("{}.{}: {}".format(i,device_id_response['devices'][i]['name'],device_id_response['devices'][i]['id']))
    
def search_user():
    artist_name = input("Enter the artist name: ")
    user_response = requests.get(SPOTIFY_USER_SEARCH,
                                headers={
                                    "Authorization" : f"Bearer {ACCESS_TOKEN}"
                                },
                                params={
                                    'q' : artist_name,
                                    'type' : 'artist'
                                }
                                )
    user_json = user_response.json()
    return user_json['artists']['items'][0]['id']

def get_alubms():
    user_id = search_user()
    user_album_response = requests.get(url="https://api.spotify.com/v1/artists/{user_id}/albums",
                                        headers={
                                            "Authorization" : f"Bearer {ACCESS_TOKEN}"
                                        }
                                        )
    user_album = user_album_response.json()
    print(user_album)


def main():
    n = 0
    while(int(n) != 4):
        n = input("select an option:\n1.get user device details\n2.get list off playlist\n3.get artist album\n4.quit\n")
        if int(n) == 1:
            get_user_device_details()
        elif int(n) == 2:
            getting_user_playlist()
        elif int(n) == 3:
            get_alubms()
            



if __name__ == '__main__':
   main()