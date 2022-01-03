from django.urls import path

from .views import ShortenUrl

urlpatterns = [
    path("", ShortenUrl.as_view(), name="home")
]
