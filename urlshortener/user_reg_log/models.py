from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name="profile")

    def __str__(self):
        return "Профиль пользователя {}".format(self.user.username)
