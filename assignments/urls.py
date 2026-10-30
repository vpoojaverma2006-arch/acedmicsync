from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_assignment, name="upload_assignment"),
    path("teacher/", views.teacher_assignments, name="teacher_assignments"),
    path("student/", views.student_assignments, name="student_assignments"),
    path(
        "download/<int:assignment_id>/",
        views.download_assignment,
        name="download_assignment"
    ),
]