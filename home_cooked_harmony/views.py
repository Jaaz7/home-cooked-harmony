from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.paginator import Paginator
from .models import Post
from cloudinary.uploader import destroy
from .forms import PostForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
    comments = post.comments.all()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            print(comment_form.errors)
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("post_details", slug=post.slug)
    else:
        comment_form = CommentForm()
    return render(
        request,
        "post_details.html",
        {"post": post, "comments": comments, "form": comment_form},
    )


@login_required
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


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html")
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.image and not "food_placeholder.png" in post.image.url:
        public_id = post.image.url.split("/")[-1].split(".")[0]

        destroy(public_id)

    post.delete()

    return redirect("home")


def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "post_list.html", {"page_obj": page_obj})

def register(request):
    return render(request, "register.html")