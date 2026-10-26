from django.contrib import admin
from django.urls import path, include
from host import views

urlpatterns = [
    # Home
    path("", views.home, name="home"),

    # Admin
    path("admin/", admin.site.urls),

    # Common Login and Registration
    path("login/", views.common_login, name="login"),
    path("register/", views.register, name="register"),

    # Host
    path("host/", include("host.urls")),

    # Teacher
    path("teacher/", include("teacher.urls")),

    # Student
    path("student/", include("student.urls")),

    # User Table
    path("usertable/", include("usertable.urls")),
]