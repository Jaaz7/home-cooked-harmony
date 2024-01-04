from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


# Create your models here.


class Post(models.Model):
    PREPTIME_CHOICES = [
        ('20', 'up to 20mn'),
        ('20-40', '20mn-40mn'),
        ('40+', '40mn+'),
    ]

    SERVINGS_CHOICES = [
        ('1-2', '1-2'),
        ('2-4', '2-4'),
        ('4+', '4+'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField("image")
    preptime = models.CharField(max_length=5, choices=PREPTIME_CHOICES, default='20')
    servings = models.CharField(max_length=3, choices=SERVINGS_CHOICES, default='1-2')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s - %s" % (self.title, str(self.author))

    def get_absolute_url(self):
        return reverse("home")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comments"
    )
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.body, self.user)
