from string import ascii_letters, digits
from random import choice

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views import View

from .models import Urls
from .forms import UrlForm
from user_reg_log.models import Profile


def redirect_to_original(request, short_url):
    """Redirect to original URL"""
    url = get_object_or_404(Urls, pk=short_url)
    return HttpResponseRedirect(url.origin_url)


def get_short_code():
    """Generate unique short address"""
    length = 7
    char = ascii_letters + digits

    while True:
        short_id = "".join(choice(char) for x in range(length))
        try:  # skip if short_id already exists
            Urls.objects.get(pk=short_id)
        except Urls.DoesNotExist:
            return short_id


class ShortenUrl(View):
    """
    Class that finds or creates a new short url in the DB
    """
    form_class = UrlForm
    template_name = 'shortener/main.html'
    title = "URL Shortner"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(
            request, self.template_name, {'form': form, "title": self.title}
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            url = form.cleaned_data["url"]

            try:  # if URL already exists
                url = Urls.objects.get(origin_url=url)

                # if user is authenticated add short_url to his profile
                if request.user.is_authenticated:
                    customer = Profile.objects.get(user=request.user)
                    url.user_profile.add(customer)

                short_url = f"{settings.SITE_URL}/{url.short_url}"
            except Urls.DoesNotExist:  # if it's new URL
                short_url = get_short_code()

                # if user is authenticated add short_url to his profile
                if request.user.is_authenticated:
                    customer = Profile.objects.get(user=request.user)
                    new_url = Urls(origin_url=url, short_url=short_url)
                    new_url.save()
                    new_url.user_profile.add(customer)
                else:
                    new_url = Urls(origin_url=url, short_url=short_url)

                new_url.save()

                short_url = f"{settings.SITE_URL}/{short_url}"

            context = {
                "title": self.title,
                "short_url": short_url,
                'form': self.form_class()
            }

            return render(request, self.template_name, context=context)

        return render(
            request, self.template_name, {'form': form, "title": self.title}
        )
