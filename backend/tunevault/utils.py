from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import uuid
import hashlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from spotipy.oauth2 import SpotifyOAuth
from .models import Vault
from dotenv import load_dotenv
from .models import Comment, Post, Profile

load_dotenv()

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_artist(id):
    result = sp.artist(id)
    return result

#se podrían pasar codigos de error para que el front los maneje
def get_result_search(search, type, limit, offset, genre = None):
    if ((type != "artist" and type !="album" and type != "playlist" and type !="track" and type !="show" and type != "episode" and type !="audiobook" and type !="member") or limit < 0 or offset < 0):
        return json.dumps({'error': 'Tipo de busqueda no valida'})

    elif(type == "member"):
        listToRet = []
        total = 0
        offset_copy = offset
        next = False
        next_flag = False
        finished = False

        for profile in Profile.objects:
            if profile.isArtist and (search in profile.user.get_username()):

                if offset_copy == 0:
                    listToRet.append(profile.user.get_username())
                    print(profile.user.get_username())
                else:
                    offset_copy -= 1

                if finished:
                    next_flag = True
                    break
                else:
                    total += 1

            if not finished and total >= limit:
                finished = True

            if next_flag:
                break

        jsonResult = {
            'type': type,
            'members': listToRet,
            'total': total,
            'next': next,
        }

    else:
        result = sp.search(search,limit,offset,type, 'ES')
        listToRet = []
        if result[type + 's']['items']==[]:
            return json.dumps({'error': 'No se encontraron artistas'})
        for items in result[type + 's']['items']:
            if (genre != None):
                if (genre in items['genres']):
                        if (items['images'] == []):
                            queryResult = {
                                'id' : items['id'],
                                type: items['name'],
                                'image': 'https://community.spotify.com/t5/image/serverpage/image-id/55829iC2AD64ADB887E2A5/image-dimensions/1700?v=v2&px=-1',
                                'likes': 0
                            }
                        else:
                            queryResult = {
                                'id' : items['id'],
                                type: items['name'],
                                'image': items['images'][0]['url'],
                                'likes': 0
                            }
                        listToRet.append(queryResult)
            else:
                if (items['images'] == []):
                    queryResult = {
                        'id' : items['id'],
                        type: items['name'],
                        'image': 'https://community.spotify.com/t5/image/serverpage/image-id/55829iC2AD64ADB887E2A5/image-dimensions/1700?v=v2&px=-1',
                        'likes': 0
                    }
                else:
                    queryResult = {
                        'id' : items['id'],
                        type: items['name'],
                        'image': items['images'][0]['url'],
                        'likes': 0
                    }
                listToRet.append(queryResult)
        jsonResult = {
            'type': type,
            'vaults': listToRet,
            'total': result[type+'s']['total'],
            'next': result[type+'s']['next'],
            'query': search
        }

    return jsonResult

#para sección de música
def search_music(query, genre = None):
    searchArtist = get_result_search(query, 'artist', 10, 0)
    searchAlbum = get_result_search(query, 'album', 10, 0)
    result = [searchArtist, searchAlbum]
    return {'result' : result }

#para seccion de podcast
def search_podcast(query):
    searchPodcast = get_result_search(query, 'show', 10, 0)
    searchEpisode = get_result_search(query, 'episode', 10, 0)
    result = [searchPodcast, searchEpisode]
    return {'result' : result }

def search_member(query):
    searchMember = get_result_search(query, 'member', 10, 0)
    result = searchMember
    return {'result' : result }

#para barra de navegación
def search_all(query):
    searchArtist = get_result_search(query, 'artist', 10, 0)
    searchAlbum = get_result_search(query, 'album', 10, 0)
    searchPodcast = get_result_search(query, 'show', 10, 0)
    searchEpisode = get_result_search(query, 'episode', 10, 0)
    searchMember = get_result_search(query, 'member', 10, 0)
    result = {searchArtist, searchAlbum, searchPodcast, searchEpisode, searchMember}
    return result

def get_or_create_vault(item):
    try:
        toRet = Vault.objects.filter(id=item['id'])
    except:
        toRet = create_vault(item['id'],item['name'],item['external_urls']['spotify'],item['genres'],item['images'][0]['url'])
    return {
        'id': toRet.id,
        'title': toRet.title,
        'vtype': vtype,
        'description': toRet.description,
        'external_url': toRet.external_url,
        'genres': toRet.genres,
        'spotifyimg':toRet.spotifyimg,
        'rating':toRet.rating,
        'followers':toRet.followers,
        'likes':toRet.likes,
        'authors': json.decoder.JSONDecoder(toRet.authors),
        'total_tracks': toRet.total_tracks,
    }

def get_or_create_by_id(vtype, id):
    type = vtype.lower()
    str = type + id
    uuid_str = string_to_uuid(str)
    toRet = None
    if type == 'artist':
        try:
            toRet = Vault.objects.get(id=uuid_str)
        except:
            item = sp.artist(id)
            artist = [{'name': item['name'], 'image': item['images'][0]['url']}]
            toRet = create_vault(item['id'], type, item['name'], 'None', item['genres'], item['images'][0]['url'], item['external_urls']['spotify'], artist, 0, 'None')
    elif type == 'podcast':
        try:
            toRet = Vault.objects.get(id=uuid_str)
        except:
            item = sp.show(id, None)
            publisher = [{'name': item['publisher'], 'image': item['images'][0]['url']}]
            toRet = create_vault(item['id'], type, item['name'], item['description'], 'None', item['images'][0]['url'], item['external_urls']['spotify'], publisher, item['total_episodes'], 'None')
    elif type == 'album':
        try:
            toRet = Vault.objects.get(id=uuid_str)
        except:
            item = sp.album(id, None)
            artists = []
            for artist in item['artists']:
                artistInfo = sp.artist(artist['id'])
                artists.append({'name': artist['name'], 'image': artistInfo['images'][0]['url']})
            toRet = create_vault(item['id'], type, item['name'], 'None', item['genres'],item['images'][0]['url'], item['external_urls']['spotify'], artists, item['total_tracks'], item['release_date'])
    else:
        pass #error
    return {
        'id': toRet.id,
        'title': toRet.title,
        'type': type,
        'description': toRet.description,
        'external_url': toRet.external_url,
        'genres': json.loads(toRet.genres),
        'spotifyimg':toRet.spotifyimg,
        'rating':toRet.rating,
        'followers':toRet.followers,
        'likes':toRet.likes,
        'authors': json.loads(toRet.authors),
        'total_tracks': toRet.total_tracks,
        'date': toRet.date,
    }

def get_album_item(id):
    pass

def get_top50_artists(offset):
    playlists = sp.playlist_tracks("37i9dQZF1DXcBWIGoYBM5M", None, 8, offset) # top50 playlist id
    list = []
    for item in playlists['items']:
        if (item['track']['artists'] not in list):
            list.append(item['track']['artists'])
    return list

def format_top50(offset):
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
    top50_dict = {}
    isLastPage = False
    while (len(top50_dict) < 9):
        top50_list = get_top50_artists(offset)
        if (len(top50_list) < 9):
            islastPage = True
        for item in top50_list:
            for artist in item:
                if artist['id'] not in top50_dict:
                    artist_data = get_artist(artist['id'])
                    top50_dict[artist['id']] = {
                        'artist': artist_data['name'],
                        'image': artist_data['images'][0]['url'],
                        'likes': 0
                    }
    return {'top': top50_dict, 'isLastPage': isLastPage}

def create_vault(id, type, title, description, genres, spotifyimg, external_url, authors, total_tracks, date):
    str = type.lower() + id
    uuid_str = string_to_uuid(str)
    vaultToRet = Vault(id=uuid_str, vtype=type, title=title, description=description, genres=json.dumps(genres), spotifyimg=spotifyimg, rating=0, followers=0, likes=0, external_url=external_url, authors=json.dumps(authors), total_tracks=total_tracks, date=date)
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


def getChainOfComments(post_id):
    comments = Comment.objects.filter(post_id=post_id)
    chain_comments = []

    for comment in comments:
        if comment.comment_answer_id == "0":
            chain_comments.append({'comment': comment, 'replies': [], 'replies_count': 0})

    for post in chain_comments:
        for comment in comments:
            if str(comment.comment_answer_id) == str(post['comment'].id):
                post['replies'].append(comment)
                post['replies_count'] += 1

    return chain_comments


def getPostsWithCommentCount(vault_id):
    posts = Post.objects.filter(vault_id=vault_id)
    posts_with_count = []
    for post in posts:
        posts_with_count.append({'post': post, 'comment_count': Comment.objects.filter(post_id=post.id).count()})
    return posts_with_count

def getVaultRating(vault_id):
    posts = Post.objects.filter(vault_id=vault_id)
    sum = 0
    count = 0
    for post in posts:
        if post.rating != 0:
            sum += post.rating
            count += 1
    return round(sum/count, 1) if count != 0 else 0

def get_profile(user):
    profile = Profile.objects.get(user__username=user)
    profile_data = {
        'user': profile.user,
        'bio': profile.bio,
        'profileimg': profile.profileimg.url,
        'location': profile.location,
        'followers': profile.followers,
    }
    return profile_data

#conectar con spotify
def get_recommended_profiles():
    profiles = Profile.objects.all()
    recommended_profiles = []
    for profile in profiles:
        #if profile.followers > 0:
        recommended_profiles.append(get_profile(profile.user))
    return {'membersList': recommended_profiles}

#se podría scrapear de algun lugar para tener un top
def get_top_podcasts(limit=10):
    topPodcastsUrls = scrap_arists(limit)

    podcasts = sp.shows(topPodcastsUrls)
    podcastsfiltered = podcasts['shows']
    podcast_data = {}
    for podcast in podcastsfiltered:
        podcast_data[podcast['id']] = {
            'artist': podcast['name'],
            'image': podcast['images'][0]['url'],
            'likes': 0
        }

    return {'top': podcast_data}

def scrap_arists(limit):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=true")
    browser = webdriver.Chrome(options=options)
    browser.get("https://podcastcharts.byspotify.com/latam")
    browser.implicitly_wait(5)
    urlList=[]
    elem= browser.find_elements(By.XPATH,'//div[@class="flex"]/div[@class="relative uppercase text-accent0 font-normal mr-4 flex justify-center items-center cursor-pointer"]/a')
    i=0
    for e in elem:
        urlList.append(e.get_attribute('href').split('/')[-1])
        i+=1
        if i==limit:
            break

    browser.quit()
    return urlList
