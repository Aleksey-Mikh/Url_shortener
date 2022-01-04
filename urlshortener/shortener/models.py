from django.db import models


class Urls(models.Model):
    short_url = models.SlugField(max_length=7, primary_key=True)
    origin_url = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    user_profile = models.ManyToManyField(
        "user_reg_log.Profile", null=True, related_name="user_profile"
    )

    def __str__(self):
        return f"origin url: {self.origin_url}, short url: {self.short_url}"

    class Meta:
        verbose_name = "URL"
        verbose_name_plural = "URLs"
        ordering = ["origin_url"]
