"""
Name: Evan Westcomb
Class: CIS 218
Date: 2/13/2026
"""

from django.shortcuts import render
from django.views.generic import ListView
from .models import Todo

class TodoListView(ListView):
    """The page view for the todo list."""
    model = Todo
    template_name = "home.html"