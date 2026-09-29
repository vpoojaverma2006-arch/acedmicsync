from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def host_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("host_dashboard")

        return render(
            request,
            "host/login.html",
            {"error": "Invalid username or password"},
        )

    return render(request, "host/login.html")


@login_required
def host_dashboard(request):
    return render(request, "host/dashboard.html")