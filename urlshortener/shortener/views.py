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
    url = get_object_or_404(Urls, pk=short_url)
    return HttpResponseRedirect(url.origin_url)


def get_short_code():
    length = 7
    char = ascii_letters + digits

    while True:
        short_id = "".join(choice(char) for x in range(length))
        try:
            Urls.objects.get(pk=short_id)
        except:
            return short_id


class ShortenUrl(View):
    form_class = UrlForm
    template_name = 'shortener/main.html'
    title = "URL Shortner"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, "title": self.title})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            url = form.cleaned_data["url"]

            try:
                url = Urls.objects.get(origin_url=url)

                if request.user.is_authenticated:
                    customer = Profile.objects.get(user=request.user)
                    url.user_profile.add(customer)

                short_url = f"{settings.SITE_URL}/{url.short_url}"
            except:
                short_url = get_short_code()

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

        return render(request, self.template_name, {'form': form, "title": self.title})
