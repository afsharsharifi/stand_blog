from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def signup_page(request):
    context = {"errors": []}
    if request.user.is_authenticated:
        return redirect(reverse("index"))
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")
        if password != re_password:
            context["errors"].append("Passwords are not match")
            return render(request, "accounts/signup.html", context)

        if User.objects.filter(username=username):
            context["errors"].append("Username already exists")
            return render(request, "accounts/signup.html", context)

        user = User.objects.create(username=username, email=email, password=password)
        login(request, user)
        return redirect(reverse("login"))
    return render(request, "accounts/signup.html")


def login_page(request):
    if request.user.is_authenticated:
        return redirect(reverse("index"))
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("index"))
    return render(request, "accounts/login.html")


def logout_page(request):
    logout(request)
    return redirect(reverse("index"))
