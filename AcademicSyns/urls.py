"""
URL configuration for AcademicSyns project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include
from host import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("host/", include("host.urls")),
    path('teacher/', include("teacher.urls")), # Student app URLs include hain
     path('usertable/', include("usertable.urls")),
]