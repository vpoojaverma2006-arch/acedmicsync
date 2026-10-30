from django.db import models
from django.contrib.auth.models import User


class Host(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="host_profile"
    )

    host_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)

    host_id = models.CharField(
        max_length=50,
        unique=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.host_name