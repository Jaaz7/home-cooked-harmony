from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("add_post/", views.add_post, name="add_post"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("search/", views.search, name="search"),
    path(
        "search_by_serving/<str:serving>/",
        views.search_by_serving,
        name="search_by_serving",
    ),
    path(
        "search_by_preptime/<str:preptime>/",
        views.search_by_preptime,
        name="search_by_preptime",
    ),
    path(
        "comment/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"
    ),
    path("post/<int:post_id>/like/", views.like_post, name="like_post"),
    path("post/<int:post_id>/delete/", views.delete_post, name="delete_post"),
    path("<slug:slug>/", views.post_detail, name="post_details"),
    path("edit_post/<int:post_id>/", views.edit_post, name="edit_post"),
]
