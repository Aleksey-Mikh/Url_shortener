from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shortener.urls")),
    path('accounts/', include('user_reg_log.urls')),
]
