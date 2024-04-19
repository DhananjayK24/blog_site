from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting_page"),
    path("posts/", views.individual_posts, name="posts_page"),
    path("/posts/<slug:slug>", views.detail_post, name="post_detail_page")
]