from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="teacher_profile"
    )

    teacher_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    mobile = models.CharField(max_length=15)

    teacher_id = models.CharField(
        max_length=50,
        unique=True
    )

    department = models.CharField(
        max_length=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.teacher_name
        



