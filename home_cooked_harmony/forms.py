from django import forms
from .models import Post, Comment

# Form class for creating or editing a Post
class PostForm(forms.ModelForm):
    # Making the image field optional
    image = forms.ImageField(required=False)

    class Meta:
        # The model that the form will interact with
        model = Post
        # Fields from the Post model to include in the form
        fields = [
            "title",
            "description",
            "image",
            "preptime",
            "servings",
        ]

# Form class for creating a Comment
class CommentForm(forms.ModelForm):
    class Meta:
        # The model that the form will interact with
        model = Comment
        # Field from the Comment model to include in the form
        fields = ["body"]
