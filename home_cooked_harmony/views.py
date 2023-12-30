from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post
from .forms import PostForm


class PostList(generic.ListView):
    queryset = Post.objects.all().order_by("-date")
    template_name = "index.html"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_view"] = "home"
        return context


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "post_details.html", {"post": post})


def add_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    return render(request, "add_post.html", {"form": form})
