"""
Name: Evan Westcomb
Class: CIS 218
Date: 2/13/2026
"""

from django.urls import path
from .views import TodoListView

urlpatterns = [
    path('', TodoListView.as_view(), name='home'),
]