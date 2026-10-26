from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# =========================
# TEACHER DASHBOARD
# =========================

@login_required
def teacher_dashboard(request):

    teacher = request.user.teacher_profile

    return render(
        request,
        "teacher/dashboard.html",
        {
            "teacher": teacher
        }
    )


# =========================
# TEACHER PROFILE
# =========================

@login_required
def teacher_profile(request):

    teacher = request.user.teacher_profile

    context = {
        "name": teacher.teacher_name,
        "staff_id": teacher.teacher_id,
        "mobile_no": teacher.mobile,
        "department": teacher.department,
        "email": teacher.email,
    }

    return render(
        request,
        "teacher_profile.html",
        context
    )