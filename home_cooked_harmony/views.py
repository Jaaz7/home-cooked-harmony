from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.
# def home(request):
#     return render(request, "index.html")


class PostList(generic.ListView):
    queryset = Post.objects.all().order_by("-date")
    template_name = "index.html"
    paginate_by = 3