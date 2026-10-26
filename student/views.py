from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def student_login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            if hasattr(user, "student_profile"):

                login(request, user)

                return redirect("student_dashboard")

            else:
                messages.error(
                    request,
                    "This account is not registered as a student."
                )

        else:
            messages.error(
                request,
                "Invalid email or password."
            )

    return render(request, "student/login.html")


@login_required
def student_dashboard(request):
    student = request.user.student_profile

    return render(
        request,
        "student/dashboard.html",
        {
            "student": student
        }
    )