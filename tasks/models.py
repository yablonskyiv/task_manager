from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


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
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.name
