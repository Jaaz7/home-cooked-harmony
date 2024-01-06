from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

# Registering the models to the admin panel
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
