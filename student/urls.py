from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.student_login, name="student_login"),
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
]