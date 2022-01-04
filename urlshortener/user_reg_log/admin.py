from django.contrib import admin
from django.conf import settings

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user_name",)
    readonly_fields = ("user_name", "short_urls",)
    fieldsets = (
        (None, {'fields': ('user_name', 'short_urls',)}),
    )

    def short_urls(self, obj):
        return "\n".join(
            [f"{settings.SITE_URL}/{a.short_url}" for a in obj.user_profile.all()]
        )

    def user_name(self, obj):
        return obj.user.username


admin.site.register(Profile, ProfileAdmin)
