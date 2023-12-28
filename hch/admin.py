from django.contrib import admin
# from .models import Post, Event, Ticket, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status")
    search_fields = ["title"]
    list_filter = ("status",)
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)
    list_display = ("title", "slug", "status", "created_on")
    search_fields = ["title", "content"]
    list_filter = (
        "status",
        "created_on",
    )
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = "content"


# Register your models here.
admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(Comment)
