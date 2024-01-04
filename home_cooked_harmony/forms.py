from django import forms
from .models import Post, Comment, Label


class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Post
        fields = [
            "title",
            "labels",
            "description",
            "image",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
