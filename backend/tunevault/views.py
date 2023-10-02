from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import ProfileSerializer, PostSerializer, CommentSerializer, VaultSerializer, UserSerializer
from .models import Profile, Post, Comment, Vault
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django_nextjs.render import render_nextjs_page_sync
from django.contrib.auth.decorators import login_required
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
from tunevault.models import Vault 
from dotenv import load_dotenv
from django.contrib.auth import authenticate, login, logout

load_dotenv()
# Create your views here.

class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class VaultView(viewsets.ModelViewSet):
    serializer_class = VaultSerializer
    queryset = Vault.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

@api_view(['POST'])
@permission_classes([AllowAny])  # Allow unauthenticated users to register
def register_user(request):
    """
    API endpoint for user registration.
    """
    if request.method == 'POST':
        # Deserialize user data
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Check if a user with the provided email already exists
            email = serializer.validated_data['email']
            if User.objects.filter(email=email).exists():
                return Response({'message': 'Email already in use'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the two provided passwords match
            password = serializer.validated_data['password']
            password_confirmation = serializer.validated_data.get('password_confirmation')
            if password != password_confirmation:
                return Response({'message': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

            # Create a new user
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                email=email,
                password=password
            )
            user.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([AllowAny])  # Allow unauthenticated users to login
def login_user(request):
    """
    API endpoint for user login.
    """
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])  # Require authentication for profile management
def profile(request):
    """
    API endpoint for user profile management.
    """
    if request.method == 'GET':
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Profile updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        request.user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

def vault(request):
    pass


auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

def search_artist(string):
    result = sp.search(string,2,0,"artist")
    listToRet = []
    if result['artists']['items']==[]:
        return json.dumps({'error': 'No se encontraron artistas'})
    for items in result['artists']['items']:
        queryResult = get_or_create_vault_(items)
        listToRet.append(queryResult)
    return listToRet

def get_or_create_vault_(item):
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
