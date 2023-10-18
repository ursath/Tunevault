from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import uuid
import hashlib
from spotipy.oauth2 import SpotifyOAuth
from .models import Vault
from dotenv import load_dotenv

load_dotenv()

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

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
    type = vtype.lower()
    str = type + id
    uuid_str = string_to_uuid(str)
    if type == 'artist':
        try:
            toRet = Vault.objects.get(id=uuid_str)
        except:
            item = sp.artist(id)
            toRet = create_vault(item['id'], type, item['name'],item['external_urls']['spotify'], item['genres'], item['images'][0]['url'])
    elif type == 'podcast':
        try:
            toRet = Vault.objects.get(id=uuid_str)
        except:
            item = sp.show(id, None)
            toRet = create_vault(item['id'], type, item['name'],item['external_urls']['spotify'], {'none'}, item['images'][0]['url'])
    elif type == 'album':
        try:
            toRet = Vault.objects.get(id=uuid_str)
        except:
            item = sp.album(id, None)
            toRet = create_vault(item['id'], type, item['name'],item['external_urls']['spotify'],item['genres'],item['images'][0]['url'])
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

def create_vault(id, type, title, description, genres, spotifyimg):
    uuid_str = string_to_uuid(id)
    vaultToRet = Vault(id=uuid_str, type=type, title=title, description=description, genres=genres, spotifyimg=spotifyimg, rating=0, followers=0, likes=0)
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