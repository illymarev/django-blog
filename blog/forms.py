from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post, Comment


class CreateUser(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username']


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)

class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]