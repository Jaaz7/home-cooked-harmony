from django.contrib.auth.models import User
from django.http import Http404
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


# Class-based view for listing posts with pagination
# and sorting by likes and date
class PostList(generic.ListView):
    queryset = Post.objects.order_by("-date")
    template_name = "index.html"
    paginate_by = 5

    # Adding extra context to the view, such as current
    # view identifier and distinct servings and prep times for search filters
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_view"] = "home"
        context["servings"] = Post.objects.values_list(
            "servings", flat=True).distinct()
        context["preptime"] = Post.objects.values_list(
            "preptime", flat=True).distinct()
        return context


# View for listing all posts in homepage with pagination
def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, {"page_obj": page_obj})


# Detailed view for a single post, including
# comments and pagination for comments
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by("-date")
    servings = Post.objects.values_list("servings", flat=True).distinct()
    preptime = Post.objects.values_list("preptime", flat=True).distinct()

    paginator = Paginator(comments, 5)
    page_number = request.GET.get("page")
    comments = paginator.get_page(page_number)

    # Handling comment submission
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


# View for adding a new post
@login_required
def add_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if ("preparation_time" not in request.POST or
                "servings" not in request.POST):
            messages.error(
                request, "You must choose a preparation"
                "time and servings amount."
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

            messages.success(request, "Post added successfully! You"
            " can view it here 👇")
            return redirect("post_details", post.slug)

    return render(request, "add_post.html", {"form": form})


# View for user login
def login_view(request):
    # Redirecting to home page if user is already logged in
    if request.user.is_authenticated:
        messages.info(request, "You're already logged in.")
        return redirect("home")

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


# View for user logout
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("home")


# View for deleting a post
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if (post.image and not "food_placeholder.png" in
    post.image.url):
        public_id = post.image.url.split("/")[-1].split(".")[0]

        destroy(public_id)

    post.delete()
    messages.success(request, "Post deleted successfully!")

    return redirect("home")


# View for registering a new user
def register(request):
    # Handling for user registration
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        # Checking if passwords match
        if password1 != password2:
            messages.error(request, "Passwords don't match.")
            return render(request, "register.html")

        # Checking if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "register.html")

        # Password validation
        try:
            validate_password(password1)
        except ValidationError as e:
            for error in e.messages:
                messages.error(request, error)
            return render(request, "register.html")

        # Creating new user
        User.objects.create_user(username=username, password=password1)
        messages.success(request, "Account created! You can log in now.")
        return redirect("login")

    # Rendering registration form
    context = {"current_view": "register"}
    return render(request, "register.html", context)


# Delete comment view
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    # Checking if the logged-in user is the author of the comment
    if request.user == comment.user:
        comment.delete()
        messages.success(request, "Comment deleted successfully!")
    # Redirecting to the post details page
    return redirect("post_details", slug=comment.post.slug)


# Like post view
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # Toggling like status
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    # Redirecting to the previous page
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


# Search view
def search(request):
    # Retrieving search query
    query = request.GET.get("q")
    # Filtering posts based on the query
    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    # Paginator
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Displaying success or warning message based on search results
    if posts:
        messages.success(request,
        f"Found {posts.count()} result(s) for '{query}'")
    else:
        messages.warning(request, f"No results found for '{query}'")
    # Context for rendering search results
    context = {}
    context["posts"] = page_obj.object_list
    context["servings"] = Post.objects.values_list(
        "servings", flat=True).distinct()
    context["preptime"] = Post.objects.values_list(
        "preptime", flat=True).distinct()
    context["page_obj"] = page_obj
    context["is_paginated"] = page_obj.has_other_pages()
    return render(request, "search_results.html", context)


# Search by serving view
def search_by_serving(request, serving):
    posts = Post.objects.filter(servings=serving)

    # Paginator
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if posts:
        messages.success(request,
        f"Found {posts.count()} result(s) for '{serving}'")
    else:
        messages.warning(request, f"No results found for '{serving}'")
    context = {}
    context["posts"] = page_obj.object_list
    context["servings"] = Post.objects.values_list(
        "servings", flat=True).distinct()
    context["preptime"] = Post.objects.values_list(
        "preptime", flat=True).distinct()
    context["page_obj"] = page_obj
    context["is_paginated"] = page_obj.has_other_pages()
    return render(request, "search_results.html", context)


# Search by preparation time view
def search_by_preptime(request, preptime):
    posts = Post.objects.filter(preptime=preptime)

    # Paginator
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if posts:
        messages.success(request,
        f"Found {posts.count()} result(s) for '{preptime}'")
    else:
        messages.warning(request, f"No results found for '{preptime}'")
    context = {}
    context["posts"] = page_obj.object_list
    context["servings"] = Post.objects.values_list(
        "servings", flat=True).distinct()
    context["page_obj"] = page_obj
    context["is_paginated"] = page_obj.has_other_pages()
    context["preptime"] = Post.objects.values_list(
        "preptime", flat=True).distinct()
    return render(request, "search_results.html", context)


# Edit post view
@login_required
def edit_post(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id)
    except Http404:
        messages.error(request,
        "You're trying to edit a post that doesn't exist.")
        return redirect("home")

    # Check if the current user is the author of the post
    if request.user != post.author:
        messages.error(request, "You don't have permission to edit this post.")
        return redirect("post_details", post.slug)

    # Handling form submission
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # Checking if any changes were made in the form
            if form.has_changed():
                form.save()
                messages.success(request, "Post updated successfully!")
                return redirect("post_details", post.slug)
            else:
                messages.info(request, "No changes were made to the post.")
    else:
        form = PostForm(instance=post)

    # Rendering the edit post form
    return render(request, "edit_post.html", {"form": form})
