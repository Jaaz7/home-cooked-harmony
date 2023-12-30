from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


# Create your views here.
# def home(request):
#     return render(request, "index.html")


class PostList(generic.ListView):
    queryset = Post.objects.all().order_by("-date")
    template_name = "index.html"
    paginate_by = 3


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "post_details.html", {"post": post})
