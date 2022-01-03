from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import UserRegisterForm, UserLoginForm


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            login(request, user)
            messages.success(request, "Регистрация прошла успешно")
            return redirect("home")
        else:
            messages.warning(request, "Ошибка регистрации")
    else:
        form = UserRegisterForm()
    return render(request, "user_reg_log/register.html", {"form": form})


def user_login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, "user_reg_log/login.html", {"form": form})


def user_logout_view(request):
    logout(request)
    return redirect("login")


def user_profile(request):
    customer = Profile.objects.get(user=request.user)
    urls = customer.user_profile.all()
    context = {
        "customer": customer,
        "urls": urls,
    }
    return render(request, "user_reg_log/user_profile.html", context)
