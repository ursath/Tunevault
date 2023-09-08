from django.shortcuts import render
<<<<<<< HEAD
from rest_framework import viewsets
from .serializers import ProfileSerializer, PostSerializer, CommentSerializer, VaultSerializer
from .models import Profile, Post, Comment, Vault

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
=======
from django.contrib.auth.models import User, auth
from .models import Profile, Post, Vault, Comment

# Create your views here.

def settings(request):
    pass

def profile(request):
    pass

def signup(request):
    pass

def signin(request):
    pass

def vault(request):
    pass
>>>>>>> 9e651f2679befcbc584fd29233e7fd95e826f13a
