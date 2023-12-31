from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ["title", "description", "image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
