from django.shortcuts import render, redirect
from .models import Profile, Post, Comment, Vault
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from .utils import get_or_create_by_id, format_top50, getChainOfComments, getPostsWithCommentCount, getVaultRating, get_recommended_profiles, get_profile, verify_artist

load_dotenv()

# Create your views here.

def home(request):
    return render(request, 'home.html')

def music(request):
    return render(request, 'music.html')

def podcasts(request):
    return render(request, 'podcasts.html')

def members(request):
    return render(request, 'members.html')

def profile(request):
    return render(request, 'profile.html')


# class CustomProviderAuthView(ProviderAuthView):
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)

#         if response.status_code == 201:
#             access_token = response.data.get('access')
#             refresh_token = response.data.get('refresh')

#             response.set_cookie(
#                 'access',
#                 access_token,
#                 max_age=settings.AUTH_COOKIE_MAX_AGE,
#                 path=settings.AUTH_COOKIE_PATH,
#                 secure=settings.AUTH_COOKIE_SECURE,
#                 httponly=settings.AUTH_COOKIE_HTTP_ONLY,
#                 samesite=settings.AUTH_COOKIE_SAMESITE
#             )
#             response.set_cookie(
#                 'refresh',
#                 refresh_token,
#                 max_age=settings.AUTH_COOKIE_MAX_AGE,
#                 path=settings.AUTH_COOKIE_PATH,
#                 secure=settings.AUTH_COOKIE_SECURE,
#                 httponly=settings.AUTH_COOKIE_HTTP_ONLY,
#                 samesite=settings.AUTH_COOKIE_SAMESITE
#             )

#         return response


# class CustomTokenObtainPairView(TokenObtainPairView):
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)

#         if response.status_code == 200:
#             access_token = response.data.get('access')
#             refresh_token = response.data.get('refresh')

#             response.set_cookie(
#                 'access',
#                 access_token,
#                 max_age=settings.AUTH_COOKIE_MAX_AGE,
#                 path=settings.AUTH_COOKIE_PATH,
#                 secure=settings.AUTH_COOKIE_SECURE,
#                 httponly=settings.AUTH_COOKIE_HTTP_ONLY,
#                 samesite=settings.AUTH_COOKIE_SAMESITE
#             )
#             response.set_cookie(
#                 'refresh',
#                 refresh_token,
#                 max_age=settings.AUTH_COOKIE_MAX_AGE,
#                 path=settings.AUTH_COOKIE_PATH,
#                 secure=settings.AUTH_COOKIE_SECURE,
#                 httponly=settings.AUTH_COOKIE_HTTP_ONLY,
#                 samesite=settings.AUTH_COOKIE_SAMESITE
#             )

#         return response


# class CustomTokenRefreshView(TokenRefreshView):
#     def post(self, request, *args, **kwargs):
#         refresh_token = request.COOKIES.get('refresh')

#         if refresh_token:
#             request.data['refresh'] = refresh_token

#         response = super().post(request, *args, **kwargs)

#         if response.status_code == 200:
#             access_token = response.data.get('access')

#             response.set_cookie(
#                 'access',
#                 access_token,
#                 max_age=settings.AUTH_COOKIE_MAX_AGE,
#                 path=settings.AUTH_COOKIE_PATH,
#                 secure=settings.AUTH_COOKIE_SECURE,
#                 httponly=settings.AUTH_COOKIE_HTTP_ONLY,
#                 samesite=settings.AUTH_COOKIE_SAMESITE
#             )

#         return response


# class CustomTokenVerifyView(TokenVerifyView):
#     def post(self, request, *args, **kwargs):
#         access_token = request.COOKIES.get('access')

#         if access_token:
#             request.data['token'] = access_token

#         return super().post(request, *args, **kwargs)


# class LogoutView(APIView):
#     def post(self, request, *args, **kwargs):
#         response = Response(status=status.HTTP_204_NO_CONTENT)
#         response.delete_cookie('access')
#         response.delete_cookie('refresh')

#         return response

# class ProfileView(viewsets.ModelViewSet):
#     serializer_class = ProfileSerializer
#     queryset = Profile.objects.all()

# class PostView(viewsets.ModelViewSet):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

# class CommentView(viewsets.ModelViewSet):
#     serializer_class = CommentSerializer
#     queryset = Comment.objects.all()

# class VaultView(viewsets.ModelViewSet):
#     serializer_class = VaultSerializer
#     queryset = Vault.objects.all()

@login_required(login_url='signin')
def settings_profile(request):

    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':

        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
            
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        return redirect('settings')
    # TODO ver que anda
    return render(request, 'settingsProfile.html', {'user_profile': user_profile})


def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})


# @login_required(login_url='signin')
# def profile(request, pk):
#     user_object = User.objects.get(username=pk)
#     user_profile = Profile.objects.get(user=user_object)
#     user_posts = Post.objects.filter(user=pk)
#     user_post_length = len(user_posts)

#     follower = request.user.username
#     user = pk

#     if FollowersCount.objects.filter(follower=follower, user=user).first():
#         button_text = 'Unfollow'
#     else:
#         button_text = 'Follow'

#     user_followers = len(FollowersCount.objects.filter(user=pk))
#     user_following = len(FollowersCount.objects.filter(follower=pk))

#     context = {
#         'user_object': user_object,
#         'user_profile': user_profile,
#         'user_posts': user_posts,
#         'user_post_length': user_post_length,
#         'button_text': button_text,
#         'user_followers': user_followers,
#         'user_following': user_following,
#     }
#     return render(request, 'profile.html', context)


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        isArtist = request.POST['isArtist']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already associated with an existing account')
                return redirect('create_account')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists, please choose another one')
                return redirect('create_account')
            elif isArtist:
                if (request.POST['spotify_url'] is not None):
                    if (verify_artist(request.POST['link']) is False):
                        messages.info("You must provide a valid Spotify profile for artists")
                        return redirect('create_account')
                else: 
                    messages.info("You must verify your Spotify profile")
                    return redirect('create_account')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id, isArtist=isArtist)
                new_profile.save()
                return redirect('profile')
        else:
            messages.info(request, 'Password not matching')
            return redirect('create_account')

    else:
        return render(request, 'createAccount.html')


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')

    else:
        return render(request, 'login.html')
    
    
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


def vault(request, vtype, id):
   # id es el ID del album/artista
   # info: id, tipo (podcast/album), nombre, artista, descripcion, foto, foto del artista, likes, duracion, canciones
    vault = get_or_create_by_id(vtype, id)
    form = PostForm(request.POST)  
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.user = request.user
        new_post.vault_id = id
        new_post.rating = form.cleaned_data['rating']
        new_post.save()
    posts = getPostsWithCommentCount(id)
    rating = getVaultRating(id)
    first_post = Post.objects.filter(user=request.user, vault_id=id).count() == 0

    context = {'vault': vault, 'posts': posts, 'form': form, 'rating':rating, 'first_post': first_post }
    return render(request, 'vault.html', context)

def gallery(request):
    # muestra los albums/artists/podcasts guardados en la bd
    # info: id, nombre, tipo, likes, fo
    list=[]
    for vault in Vault.objects.all():
        list.append({"id":vault.id, "title":vault.title, "vtype":vault.vtype, "likes":vault.likes, "spotifyimg":vault.spotifyimg})
    return render(request, 'gallery.html', {list})


def music(request):
    context = format_top50(0)
    return render(request, 'music.html', context)

def members(request):
    context = get_recommended_profiles()
    return render(request, 'members.html', context)

def member(request, user):
    user_profile = get_profile(user)
    return render(request, 'profile.html', {'user_profile': user_profile})

class vaultPost(View):
    def get(self, request, post_id, *args, **kwargs):
        
        comment_count = Comment.objects.filter(post_id=post_id).count()
        chain_comments = getChainOfComments(post_id)
        post = Post.objects.get(id=post_id)
        form = CommentForm()

        context = {
            'post': post,
            'form': form,
            'comments': chain_comments,
            'comment_count': comment_count,
        }
        return render(request, 'post.html', context)
    
    def post(self, request, post_id, *args, **kwargs):
        post = Post.objects.get(id=post_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post_id = post_id
            new_comment.save()
        
        comment_count = Comment.objects.filter(post_id=post_id).count()
        chain_comments = getChainOfComments(post_id)

        context = {
            'post': post,
            'form': form,
            'comments': chain_comments,
            'comment_count': comment_count,
        }

        return render(request, 'post.html', context)
    

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)