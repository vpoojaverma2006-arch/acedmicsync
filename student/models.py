from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    student_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    roll_number = models.CharField(max_length=50, unique=True)
    course = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    student_id = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name