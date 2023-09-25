from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_image', default='profile_image.jpg')
    location = models.CharField(max_length=100, blank=True)
    followers = models.PositiveIntegerField(default = 0)
    # TODO guardar artistas/albumes favoritos

    def __str__(self):
        return self.user.username

class Vault(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.TextField(max_length=150)
    description = models.TextField(default = "this is the vault description")
    genres = models.TextField(default = "here are the genres")
    rating = models.FloatField(default = 0)
    spotifyimg = models.ImageField(upload_to= 'vault_image', default='unknown_vault.jpg')
    followers = models.PositiveIntegerField(default = 0)
    likes = models.PositiveIntegerField(default = 0)
    # TODO sacar mas info de la api de spotify
    def __str__(self):
        return self.title

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=50)
    # TODO relacionar las foreign keys
    # TODO ver la longitud del id
    vault_id = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    date = models.DateField(default=datetime.now)
    title = models.TextField(max_length=60)
    content = models.TextField(max_length=597)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=50)
    # TODO relacionar las foreign keys
    post_id = models.CharField(max_length=50)
    comment_answer_id = models.CharField(max_length=50, default=0)
    # si es respuesta directa al post -> 0
    # si contesta a un comentario -> id del comentario y del post
    # TODO mejorar comentarios de comentarios
    likes = models.IntegerField(default=0)
    date = models.DateField(default=datetime.now)
    content = models.TextField(max_length=597)

    def __str__(self):
        return self.user.username