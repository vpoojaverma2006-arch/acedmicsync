from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.host_login, name="host_login"),
    path("dashboard/", views.host_dashboard, name="host_dashboard"),
    path("bulk-student/", views.bulk_student, name="bulk_student"),
    path("register/", views.host_register, name="host_register"),
]