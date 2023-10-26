from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '2',
            'placeholder': 'Say Something...'
            }))

    class Meta:
        model = Post
        fields = ['title']


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '2',
            'placeholder': 'Reply to this post...',
        }))

    class Meta:
        model = Comment
        fields = ['content']