from django.db import models
from django.contrib.auth.models import User


class Assignment(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    file = models.FileField(upload_to='assignments/')

    due_date = models.DateField()
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='uploaded_assignments'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['due_date', '-created_at']