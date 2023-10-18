from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import uuid
import hashlib
from spotipy.oauth2 import SpotifyOAuth
# from .models import Vault
from dotenv import load_dotenv

load_dotenv()

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_artist(id):
    result = sp.artist(id)
    return result

def get_artist_search(string):
    result = sp.search(string,1,0,"artist")
    listToRet = []
    if result['artists']['items']==[]:
        return json.dumps({'error': 'No se encontraron artistas'})
    for items in result['artists']['items']:
        queryResult = get_or_create_vault(items)
        listToRet.append(queryResult)
    return listToRet

def get_or_create_vault(item):
    try:
        toRet = Vault.objects.filter(id=item['id'])
    except:
        toRet = create_vault(item['id'],item['name'],item['external_urls']['spotify'],item['genres'],item['images'][0]['url'])
    return {
        'id': toRet.id,
        'title': toRet.title,
        'description': toRet.description,
        'genres': toRet.genres,
        'spotifyimg':toRet.spotifyimg,
        'rating':toRet.rating,
        'followers':toRet.followers,
        'likes':toRet.likes
    }

def get_or_create_by_id(vtype, id):
    if vtype == 'Artist':
        pass
    elif vtype == 'Podcast':
        pass
    elif vtype == 'Album':
        try:
            uuid_str = string_to_uuid(id)
            print(uuid_str)
            toRet = Vault.objects.get(id=uuid_str)
        except:
            item = sp.album(id, None)
            toRet = create_vault(item['id'],item['name'],item['external_urls']['spotify'],item['genres'],item['images'][0]['url'])
    else:
        pass #error
    return {
        'id': toRet.id,
        'title': toRet.title,
        'vtype': vtype,
        'description': toRet.description,
        'genres': toRet.genres,
        'spotifyimg':toRet.spotifyimg,
        'rating':toRet.rating,
        'followers':toRet.followers,
        'likes':toRet.likes
    }

def get_album_item(id):
    pass

def get_top50_artists():
    playlists = sp.playlist_tracks("37i9dQZF1DXcBWIGoYBM5M") # top50 playlist id
    list = []
    for item in playlists['items']:
        list.append(item['track']['artists'])
    return list

def format_top50():
    # formats data from get_top50_artists() in the following way 
    # {
    #     'id_artist_1': {
    #         'artist': 'artist',
    #         'image': 'artistimg',
    #         'likes': 0
    #     },
    #     'id_artist_2': {
    #         'artist': 'artist',
    #         'image': 'artistimg',
    #         'likes': 0
    #     },
    #     }
    # }
    top50_list = get_top50_artists()
    top50_dict = {}
    for item in top50_list:
        for artist in item:
            if artist['id'] not in top50_dict:
                artist_data = get_artist(artist['id'])
                top50_dict[artist['id']] = {
                    'artist': artist_data['name'],
                    'image': artist_data['images'][0]['url'],
                    'likes': 0
                }
            else:
                top50_dict[artist['id']]['likes'] += 1
    return top50_dict

def create_vault(id, title, description, genres, spotifyimg):
    uuid_str = string_to_uuid(id)
    vaultToRet = Vault(id=uuid_str, title=title, description=description, genres=genres, spotifyimg=spotifyimg, rating=0, followers=0, likes=0)
    vaultToRet.save()
    return vaultToRet

def string_to_uuid(input_string):
    # Hash the input string using SHA-256
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()

    # Take the first 32 characters of the hash (128 bits)
    hash_32_chars = sha256_hash[:32]

    # Convert the 32-character hexadecimal string to UUID format
    uuid_string = '-'.join([
        hash_32_chars[:8],  # First 8 characters
        hash_32_chars[8:12],  # Next 4 characters
        hash_32_chars[12:16],  # Next 4 characters
        hash_32_chars[16:20],  # Next 4 characters
        hash_32_chars[20:]  # Last 12 characters
    ])

    # Create a UUID from the formatted string
    try:
        uuid_param = uuid.UUID(uuid_string)
        return uuid_param
    except ValueError:
        # Handle the case where the string is not a valid UUID
        return None  # Or raise an error or handle it as needed
    


def main():
    # #print(get_top50_artists())
    # format_top50()
    # ans = get_artist('5H4yInM5zmHqpKIoMNAx4r')
    print(format_top50())

if __name__ == "__main__":
    main()