from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.host_login, name="host_login"),
    path("dashboard/", views.host_dashboard, name="host_dashboard"),
]