from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("add_post/", views.add_post, name="add_post"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("<slug:slug>/", views.post_detail, name="post_details"),
]
