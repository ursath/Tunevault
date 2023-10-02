from rest_framework import serializers
from .models import Profile, Post, Comment, Vault
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id_user', 'user', 'bio', 'profileimg', 'location')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'vault_id', 'likes', 'date', 'title', 'content')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'post_id', 'comment_answer_id', 'likes', 'date', 'content')

class VaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vault
        fields = ('id', 'title', 'description', 'genres', 'rating', 'spotifyimg', 'followers', 'likes')

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)  # write_only for security
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        """
        Custom validation to ensure that the password and password_confirmation match.
        """
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError("Passwords do not match")

        return data

    def create(self, validated_data):
        """
        Create and return a new User instance.
        """
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return user



