from django.shortcuts import render
from django.views.generic import ListView
from .models import Todo

class TodoListView(ListView):
    """Page view for the todo list."""
    model = Todo
    template_name = "home.html"