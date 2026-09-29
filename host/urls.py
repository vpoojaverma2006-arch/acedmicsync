from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.host_login, name="host_login"),
    path("dashboard/", views.host_dashboard, name="host_dashboard"),
]