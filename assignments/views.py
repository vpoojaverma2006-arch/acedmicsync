from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist

from .models import Assignment
from .forms import AssignmentForm


# Teacher: Upload Assignment
@login_required
def upload_assignment(request):
    if not hasattr(request.user, "teacher_profile"):
        messages.error(
            request,
            "Only teachers can upload assignments."
        )
        return redirect("login")

    if request.method == "POST":
        form = AssignmentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.uploaded_by = request.user
            assignment.save()

            messages.success(
                request,
                "Assignment uploaded successfully!"
            )
            return redirect("teacher_assignments")
    else:
        form = AssignmentForm()

    return render(
        request,
        "assignments/upload_assignment.html",
        {"form": form}
    )


# Teacher: View Uploaded Assignments
@login_required
def teacher_assignments(request):
    if not hasattr(request.user, "teacher_profile"):
        return redirect("login")

    assignments = Assignment.objects.filter(
        uploaded_by=request.user
    )

    return render(
        request,
        "assignments/teacher_assignments.html",
        {"assignments": assignments}
    )


# Student: View All Assignments
@login_required
def student_assignments(request):
    if not hasattr(request.user, "student_profile"):
        return redirect("login")

    assignments = Assignment.objects.all()

    return render(
        request,
        "assignments/student_assignments.html",
        {"assignments": assignments}
    )


# Student/Teacher: Secure File Download
@login_required
def download_assignment(request, assignment_id):
    assignment = get_object_or_404(
        Assignment,
        id=assignment_id
    )

    is_teacher = hasattr(
        request.user, "teacher_profile"
    )
    is_student = hasattr(
        request.user, "student_profile"
    )

    if not (is_teacher or is_student):
        raise Http404("Assignment not found.")

    if is_teacher and not is_student:
        if assignment.uploaded_by_id != request.user.id:
            raise Http404("Assignment not found.")

    try:
        file_handle = assignment.file.open("rb")
        return FileResponse(
            file_handle,
            as_attachment=True,
            filename=assignment.file.name.split("/")[-1]
        )
    except (FileNotFoundError, ValueError):
        raise Http404("Assignment file not found.")