from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=500)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)

    class Priority(models.TextChoices):
        URGENT = "urgent", "Urgent"
        HIGH = "hi", "High"
        MEDIUM = "medium", "Medium"
        LOW = "low", "Low"

    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )