from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.teacher_register, name="teacher_register"),
    path("profile/", views.teacher_profile, name="teacher_profile"),
    path("dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
]