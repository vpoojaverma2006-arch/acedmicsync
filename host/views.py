from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import transaction
from django.utils.crypto import get_random_string

import openpyxl

from student.models import Student


# =========================
# HOME PAGE
# =========================

def home(request):
    return render(request, "host/home.html")


# =========================
# COMMON LOGIN
# =========================

def common_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            # STUDENT
            if hasattr(user, "student_profile"):
                return redirect("student_dashboard")

            # TEACHER
            if hasattr(user, "teacher_profile"):
                return redirect("teacher_dashboard")

            # HOST
            if user.is_staff:
                return redirect("host_dashboard")

            return render(
                request,
                "host/login.html",
                {
                    "error": "Your account role is not configured."
                }
            )

        return render(
            request,
            "host/login.html",
            {
                "error": "Invalid username or password."
            }
        )

    return render(
        request,
        "host/login.html"
    )


# =========================
# REGISTER PAGE
# =========================

def register(request):

    return render(
        request,
        "host/register.html"
    )


# =========================
# OLD HOST LOGIN
# =========================

def host_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("host_dashboard")

        return render(
            request,
            "host/login.html",
            {
                "error": "Invalid username or password."
            }
        )

    return render(
        request,
        "host/login.html"
    )


# =========================
# HOST DASHBOARD
# =========================

@login_required
def host_dashboard(request):

    return render(
        request,
        "host/dashboard.html"
    )


# =========================
# BULK STUDENT REGISTRATION
# =========================

@login_required
def bulk_student(request):

    if request.method == "POST":

        excel_file = request.FILES.get("excel_file")

        if not excel_file:

            return render(
                request,
                "host/bulk_student.html",
                {
                    "error": "Please select an Excel file."
                }
            )

        if not excel_file.name.endswith(".xlsx"):

            return render(
                request,
                "host/bulk_student.html",
                {
                    "error": "Only .xlsx Excel files are allowed."
                }
            )

        try:

            workbook = openpyxl.load_workbook(excel_file)
            sheet = workbook.active

            created = 0
            failed = []

            for row_number, row in enumerate(
                sheet.iter_rows(
                    min_row=2,
                    values_only=True
                ),
                start=2
            ):

                try:

                    (
                        student_name,
                        email,
                        mobile,
                        roll_number,
                        course,
                        semester,
                        student_id
                    ) = row[:7]

                    # Required fields check
                    if not all([
                        student_name,
                        email,
                        mobile,
                        roll_number,
                        course,
                        semester,
                        student_id
                    ]):

                        raise ValueError(
                            "Missing required field"
                        )

                    # Email check
                    if User.objects.filter(
                        username=email
                    ).exists():

                        raise ValueError(
                            "Email already registered"
                        )

                    # Roll number check
                    if Student.objects.filter(
                        roll_number=roll_number
                    ).exists():

                        raise ValueError(
                            "Roll number already exists"
                        )

                    # Student ID check
                    if Student.objects.filter(
                        student_id=student_id
                    ).exists():

                        raise ValueError(
                            "Student ID already exists"
                        )

                    # Temporary password
                    temporary_password = get_random_string(
                        length=10
                    )

                    # Semester conversion
                    semester_number = int(
                        str(semester)
                        .strip()
                        .upper()
                        .replace("TH", "")
                        .replace("ST", "")
                        .replace("ND", "")
                        .replace("RD", "")
                    )

                    with transaction.atomic():

                        # Create login account
                        user = User.objects.create_user(
                            username=email,
                            email=email,
                            password=temporary_password
                        )

                        # Create student profile
                        Student.objects.create(
                            user=user,
                            student_name=student_name,
                            email=email,
                            mobile=str(mobile),
                            roll_number=roll_number,
                            course=course,
                            semester=semester_number,
                            student_id=student_id
                        )

                    created += 1

                except Exception as e:

                    failed.append(
                        f"Row {row_number}: {str(e)}"
                    )

            return render(
                request,
                "host/bulk_student.html",
                {
                    "success": (
                        f"{created} student account(s) "
                        "created successfully."
                    ),
                    "failed": failed,
                }
            )

        except Exception:

            return render(
                request,
                "host/bulk_student.html",
                {
                    "error": (
                        "Invalid Excel file. "
                        "Please check the file format."
                    )
                }
            )

    return render(
        request,
        "host/bulk_student.html"
    )