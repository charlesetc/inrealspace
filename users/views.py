from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import RealSpaceUser
from .forms import CustomUserCreationForm

def dashboard(request):
    return render(request, "dashboard.html")

def index(request):
    if request.user.is_authenticated:
        return dashboard(request)
    return render(request, "landing.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "register.html",
            {"form": CustomUserCreationForm()}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("index"))
        else:
            return render(
                request, "register.html",
                {"form": form}
            )

@login_required
def profile(request, id):
    user = get_object_or_404(RealSpaceUser, id=id)
    return render(request, "profile.html", {"user": user})
