from django.urls import path
from . import views

urlpatterns = [
    # Lists all posts using a class-based view to the home page
    path("", views.PostList.as_view(), name="home"),
    
    # Route for adding a new post
    path("add_post/", views.add_post, name="add_post"),

    # Login page
    path("login/", views.login_view, name="login"),

    # Logout page, redirects user upon logout
    path("logout/", views.logout_view, name="logout"),

    # Registration page
    path("register/", views.register, name="register"),

    # Search functionality
    path("search/", views.search, name="search"),

     # Search posts by serving size, with serving size passed as a URL parameter
    path(
        "search_by_serving/<str:serving>/",
        views.search_by_serving,
        name="search_by_serving",
    ),

    # Search posts by preparation time, with preparation time passed as a URL parameter
    path(
        "search_by_preptime/<str:preptime>/",
        views.search_by_preptime,
        name="search_by_preptime",
    ),

    # Route for deleting a comment, identified by comment_id
    path(
        "comment/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"
    ),

    # Route for liking a post, identified by post_id
    path("post/<int:post_id>/like/", views.like_post, name="like_post"),

    # Route for deleting a post, identified by post_id
    path("post/<int:post_id>/delete/", views.delete_post, name="delete_post"),

    # Detailed view of a single post, identified by a slug
    path("<slug:slug>/", views.post_detail, name="post_details"),

    # Route for editing a post, identified by post_id
    path("edit_post/<int:post_id>/", views.edit_post, name="edit_post"),
]
