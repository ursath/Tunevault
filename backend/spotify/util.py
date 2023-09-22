from django.utils import timezone
from datetime import timedelta
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
from tunevault.models import Vault ## TODO arreglar import



auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_artist_search(strn):

    result=sp.search(strn,1,0,"artist")
    Ltoret=[]
    if result['artists']['items']==[]:
        return json.dumps({'error': 'No se encontraron artistas'})
    for items in result['artists']['items']:
        qresult=get_o_create_vault_(items)
        Ltoret.append(qresult)
    return Ltoret

def get_o_create_vault_(item):
    try:
        toret=Vault.objects.get(id=item['id'])
    except:
        toret=create_vault(item['id'],item['name'],item['external_urls']['spotify'],item['genres'],item['images'][0]['url'])
    return {
        'id': toret.id,
        'title': toret.title,
        'description': toret.description,
        'genres': toret.genres,
        'spotifyimg':toret.spotifyimg,
        'rating':toret.rating,
        'followers':toret.followers,
        'likes':toret.likes
    }

def get_top50_artistas():
    playlists=sp.playlist_tracks("37i9dQZF1DXcBWIGoYBM5M")#top50 playlist id
    L=[]
    for i in playlists['items']:
        L.append(i['track']['artists'])
    return L

def create_vault(id, title, description, genres, spotifyimg):
    vaulttoret = Vault(id=id, title=title, description=description, genres=genres, spotifyimg=spotifyimg, rating=0, followers=0, likes=0)
    vaulttoret.save()
    return vaulttoret


print(get_artist_search("Kanye"))
