from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoTests(TestCase):
    """Tests the todos in the todo list."""

    @classmethod
    def setUpTestData(cls):
        """Sets up a todo in the todo list for testing."""
        cls.todo = Todo.objects.create(name="This is a test todo", complete_by="Jan. 1, 2030")

    def test_model_content(self):
        """Tests the content of the model."""
        self.assertEqual(self.todo.name, "This is a test todo")
        self.assertEqual(self.todo.complete_by, "Jan. 1, 2030")

    def test_url_exists_at_correct_location(self):
        """Tests that the home URL exists in the correct location."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        """Test the homepage to see if it loads the right content and template."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "This is a test todo")