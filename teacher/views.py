from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.utils import timezone

from .models import Teacher
from student.models import Student
from assignments.models import Assignment


# TEACHER REGISTRATION
def teacher_register(request):
    if request.method == "POST":
        name = request.POST.get("teacher_name", "").strip()
        email = request.POST.get("email", "").strip().lower()
        mobile = request.POST.get("mobile", "").strip()
        teacher_id = request.POST.get("teacher_id", "").strip()
        department = request.POST.get("department", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not all([
            name, email, mobile, teacher_id,
            department, password, confirm_password
        ]):
            messages.error(request, "Please fill in all fields.")

        elif password != confirm_password:
            messages.error(request, "Passwords do not match.")

        elif len(password) < 8:
            messages.error(request, "Password must be at least 8 characters.")

        elif User.objects.filter(username=email).exists():
            messages.error(request, "This email is already registered.")

        elif Teacher.objects.filter(teacher_id=teacher_id).exists():
            messages.error(request, "Teacher ID already exists.")

        elif Teacher.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")

        else:
            try:
                with transaction.atomic():
                    user = User.objects.create_user(
                        username=email,
                        email=email,
                        password=password
                    )

                    Teacher.objects.create(
                        user=user,
                        teacher_name=name,
                        email=email,
                        mobile=mobile,
                        teacher_id=teacher_id,
                        department=department
                    )

                messages.success(
                    request,
                    "Teacher registration successful. Please log in."
                )
                return redirect("login")

            except Exception:
                messages.error(
                    request,
                    "Registration could not be completed. Please try again."
                )

    return render(request, "teacher/register.html")


# TEACHER DASHBOARD
@login_required
def teacher_dashboard(request):

    try:
        teacher = request.user.teacher_profile

    except Teacher.DoesNotExist:
        messages.error(
            request,
            "This account is not registered as a teacher."
        )
        return redirect("login")

    # Assignments uploaded by this teacher
    my_assignments = Assignment.objects.filter(
        uploaded_by=request.user
    )

    # Students belonging to the teacher's department
    # Department and course names must match
    my_students = Student.objects.filter(
        course__iexact=teacher.department
    )

    today = timezone.localdate()

    # Upcoming assignments
    upcoming_assignments = my_assignments.filter(
        due_date__gte=today
    )

    # Unique subjects from teacher's assignments
    my_subjects = (
        my_assignments
        .values_list("subject", flat=True)
        .distinct()
    )

    # Recent assignments
    recent_assignments = my_assignments.order_by(
        "-created_at"
    )[:5]

    context = {
        "teacher": teacher,

        "total_students": my_students.count(),

        "total_assignments": my_assignments.count(),

        "upcoming_assignments": upcoming_assignments.count(),

        "total_subjects": my_subjects.count(),

        "recent_assignments": recent_assignments,

        "my_students": my_students[:5],

        "my_subjects": my_subjects,
    }

    return render(
        request,
        "teacher/dashboard.html",
        context
    )


# TEACHER PROFILE
@login_required
def teacher_profile(request):

    try:
        teacher = request.user.teacher_profile

    except Teacher.DoesNotExist:
        messages.error(
            request,
            "This account is not registered as a teacher."
        )
        return redirect("login")

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