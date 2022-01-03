from django.urls import path

from .views import ShortenUrl, redirect_to_original

urlpatterns = [
    path("<str:short_url>", redirect_to_original),
    path("", ShortenUrl.as_view(), name="home")
]
