from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
from tunevault.models import Vault 
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
        toRet = Vault.objects.get(id=item['id'])
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
    try:
        toRet = Vault.objects.get(id=id)
    except:
        if vtype == 'artist':
            pass
        elif vtype == 'podcast':
            pass
        elif vtype == 'album':
            toRet = create_vault(item['id'],item['name'],item['external_urls']['spotify'],item['genres'],item['images'][0]['url'])
        else:
            pass #error
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

def get_album_item(id):
    pass

def get_top50_artists():
    playlists = sp.playlist_tracks("37i9dQZF1DXcBWIGoYBM5M")#top50 playlist id
    list = []
    for item in playlists['items']:
        list.append(item['track']['artists'])
    return list

def create_vault(id, title, description, genres, spotifyimg):
    vaultToRet = Vault(id=id, title=title, description=description, genres=genres, spotifyimg=spotifyimg, rating=0, followers=0, likes=0)
    vaultToRet.save()
    return vaultToRet
