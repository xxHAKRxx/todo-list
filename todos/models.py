"""
Name: Evan Westcomb
Class: CIS 218
Date: 2/13/2026
"""

from django.db import models

class Todo(models.Model):
    """A model that represents an item in the todo list."""
    name = models.CharField(max_length=150)
    complete_by = models.DateField()

    def __str__(self):
        return f"{self.name} {self.complete_by}"