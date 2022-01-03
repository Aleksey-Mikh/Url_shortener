from string import ascii_letters, digits
from random import choice

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views import View

from .models import Urls
from .forms import UrlForm


class ShortenUrl(View):
    form_class = UrlForm
    template_name = 'shortener/main.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
            print(url)
            return redirect("home")

        return render(request, self.template_name, {'form': form})
