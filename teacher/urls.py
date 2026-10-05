from django.urls import path
from . import views

urlpatterns = [
    path('teacher-profile/', views.teacher_profile, name='teacher_profile'),
]