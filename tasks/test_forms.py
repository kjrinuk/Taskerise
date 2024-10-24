from django.test import TestCase
from django.contrib.auth.models import User
from .forms import TaskForm
from .models import Task
import datetime

# Create test for TaskForm to test for valid and invalid data
# Allocating tasks to the logged in user
class TestTaskForm(TestCase):

    def setUp(self):
        # Create a test user to allocate tasks to
        self.user = User.objects.create_user(username="TaskUser", password="password")

    def test_taskform_is_valid(self):
        # Add some valid sample data 
        task_form = TaskForm({'task_id': 1, 'title': 'Task Title', 'description': 'Description for Task', 'due_date': datetime.date.today(), 'priority': Task.Priority.MEDIUM, 'status': Task.Status.IN_PROGRESS, 'completed': False})
        
        # Validation
        self.assertTrue(task_form.is_valid())
        
    def test_taskform_not_valid(self):
        # Add some valid sample data 
        task_form = TaskForm({'task_id': 2, 'title': '', 'description': 'Descriptifon for Task', 'due_date': datetime.date.today(), 'priority': Task.Priority.MEDIUM, 'status': Task.Status.IN_PROGRESS, 'completed': False})
        
        # Check that not valid
        self.assertFalse(task_form.is_valid(), msg='Title should be missing')
        print(task_form.errors)
        