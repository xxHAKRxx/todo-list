from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=150)
    complete_by = models.DateTimeField()

    def __str__(self):
        return f"{self.name} {self.complete_by}"