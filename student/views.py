from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def student_login(request):
    if request.user.is_authenticated:
        try:
            request.user.student_profile
            return redirect("student_dashboard")
        except ObjectDoesNotExist:
            pass

    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:
            try:
                student = user.student_profile
            except ObjectDoesNotExist:
                messages.error(
                    request,
                    "This account has no Student profile. Please contact your Host."
                )
                return render(request, "student/login.html")

            login(request, user)
            return redirect("student_dashboard")

        messages.error(request, "Invalid email or password.")

    return render(request, "student/login.html")


@login_required
def student_dashboard(request):
    try:
        student = request.user.student_profile
    except ObjectDoesNotExist:
        messages.error(
            request,
            "Student profile not found. Please log in with a valid Student account."
        )
        logout(request)
        return redirect("student_login")

    return render(
        request,
        "student/dashboard.html",
        {"student": student}
    )