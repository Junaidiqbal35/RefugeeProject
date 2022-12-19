from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SignUpForm


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "registration/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "registration/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
