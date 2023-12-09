from django.urls import path
from . import views

urlpatterns = [
    path("", views.postlist, name="postlist"),
    path("a/", views.a, name="a"),
    path("b/", views.b, name="b"),
    path("create/", views.create_post, name="create_post"),
]