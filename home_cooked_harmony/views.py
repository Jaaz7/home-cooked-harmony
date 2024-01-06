from django.contrib.auth.models import User
from django.db.models import Q, Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.paginator import Paginator
from .models import Post, Comment
from cloudinary.uploader import destroy
from .forms import PostForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class PostList(generic.ListView):
    queryset = Post.objects.annotate(likes_count=Count("likes")).order_by(
        "-likes_count", "-date"
    )
    template_name = "index.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_view"] = "home"
        context["servings"] = Post.objects.values_list("servings", flat=True).distinct()
        context["preptime"] = Post.objects.values_list("preptime", flat=True).distinct()
        return context


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by("-date")
    servings = Post.objects.values_list("servings", flat=True).distinct()
    preptime = Post.objects.values_list("preptime", flat=True).distinct()

    paginator = Paginator(comments, 5)
    page_number = request.GET.get("page")
    comments = paginator.get_page(page_number)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            print(comment_form.errors)
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request, "Comment submitted successfully!")
            return redirect("post_details", slug=post.slug)
    else:
        comment_form = CommentForm()
    return render(
        request,
        "post_details.html",
        {
            "post": post,
            "comments": comments,
            "form": comment_form,
            "servings": servings,
            "preptime": preptime,
        },
    )


@login_required
def add_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if "preparation_time" not in request.POST or "servings" not in request.POST:
            messages.error(
                request, "You must choose a preparation time and servings amount."
            )
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # Generate a unique slug if slug already exists
            slug = slugify(post.title)
            unique_slug = slug
            num = 1

            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = "{}-{}".format(slug, num)
                num += 1

            post.slug = unique_slug

            post.save()

            messages.success(request, "Post added successfully! You can view it here 👇")
            return redirect("post_details", post.slug)

    return render(request, "add_post.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "" or password == "":
            messages.error(request, "You must enter a username and password.")
            return render(request, "login.html")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {username}!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html")
    else:
        context = {"current_view": "login"}
        return render(request, "login.html", context)


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("home")


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.image and not "food_placeholder.png" in post.image.url:
        public_id = post.image.url.split("/")[-1].split(".")[0]

        destroy(public_id)

    post.delete()
    messages.success(request, "Post deleted successfully!")

    return redirect("home")


def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, {"page_obj": page_obj})


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "Passwords don't match.")
            return render(request, "register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "register.html")

        try:
            validate_password(password1)
        except ValidationError as e:
            for error in e.messages:
                messages.error(request, error)
            return render(request, "register.html")

        User.objects.create_user(username=username, password=password1)
        messages.success(request, "Account created! You can log in now.")
        return redirect("login")

    context = {"current_view": "register"}
    return render(request, "register.html", context)


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        comment.delete()
        messages.success(request, "Comment deleted successfully!")
    return redirect("post_details", slug=comment.post.slug)


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


def search(request):
    query = request.GET.get("q")
    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    if posts:
        messages.success(request, f"Found {posts.count()} result(s) for '{query}'")
    else:
        messages.warning(request, f"No results found for '{query}'")
    context = {}
    context["posts"] = posts
    context["servings"] = Post.objects.values_list("servings", flat=True).distinct()
    context["preptime"] = Post.objects.values_list("preptime", flat=True).distinct()
    return render(request, "search_results.html", context)


def search_by_serving(request, serving):
    posts = Post.objects.filter(servings=serving)
    if posts:
        messages.success(request, f"Found {posts.count()} result(s) for '{serving}'")
    else:
        messages.warning(request, f"No results found for '{serving}'")
    context = {}
    context["posts"] = posts
    context["servings"] = Post.objects.values_list("servings", flat=True).distinct()
    context["preptime"] = Post.objects.values_list("preptime", flat=True).distinct()
    return render(request, "search_results.html", context)


def search_by_preptime(request, preptime):
    posts = Post.objects.filter(preptime=preptime)
    if posts:
        messages.success(request, f"Found {posts.count()} result(s) for '{preptime}'")
    else:
        messages.warning(request, f"No results found for '{preptime}'")
    context = {}
    context["posts"] = posts
    context["servings"] = Post.objects.values_list("servings", flat=True).distinct()
    context["preptime"] = Post.objects.values_list("preptime", flat=True).distinct()
    return render(request, "search_results.html", context)


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Check if the current user is the author of the post
    if request.user != post.author:
        messages.error(request, "You don't have permission to edit this post.")
        return redirect("post_details", post.slug)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            if form.has_changed():
                form.save()
                messages.success(request, "Post updated successfully!")
                return redirect("post_details", post.slug)
            else:
                messages.info(request, "No changes were made to the post.")
    else:
        form = PostForm(instance=post)

    return render(request, "edit_post.html", {"form": form})
