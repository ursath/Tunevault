from django.utils import timezone
from datetime import timedelta
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
import tunevault
auth_manager = SpotifyClientCredentials()
BASE_URL = "https://api.spotify.com/v1/me/"

def get_artist_search(strn):
    sp = spotipy.Spotify(auth_manager=auth_manager)
    result=sp.search(strn,5,0,"artist")
    if result['artists']['items']==[]:
        return json.dumps({'error': 'No se encontraron artistas'})
    return result['artists']['items']

def get_top50_artistas():
    sp = spotipy.Spotify(auth_manager=auth_manager)
    playlists=sp.playlist_tracks("37i9dQZF1DXcBWIGoYBM5M")#top50 playlist id
    L=[]
    for i in playlists['items']:
        L.append(i['track']['artists'])
    return L

def create_vault(id,title,description,genres,spotifyimg):
    vault=tunevault.models.Vault(id=id,title=title,description=description,genres=genres,spotifyimg=spotifyimg,rating=0,followers=0,likes=0)
    vault.save()
    return vault


