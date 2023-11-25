from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<title>", views.entry_by_title, name="entry_by_title"),
    path("search/", views.search, name="search")
]
