from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import TaskForm
from .models import Task
import datetime

# Create test for TaskForm to test for authorised use
class TestTaskView(TestCase):
        
    def setUp(self):
        # Create 2 users for testing security
        self.user = User.objects.create_user(username='TaskUser', password='password')
        self.another_user = User.objects.create_user(username='AnotherUser', password='password')

        # Log in the user
        self.client.login(username='TaskUser', password='password')

        # Create a task for the logged-in user
        self.task = Task.objects.create(
            title="User Task",
            description="Sample Description",
            user=self.user,
            priority=Task.Priority.MEDIUM,
            status=Task.Status.TO_DO,
            completed=False
        )
        
        # Create another task for another user who is not logged in
        self.other_task = Task.objects.create(
            title="Another User Task",
            description="Another Description",
            user=self.another_user,
            priority=Task.Priority.LOW,
            status=Task.Status.IN_PROGRESS,
            completed=False
        )
    def test_get_tasks(self):
        # Test user can view their tasks
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User Task")  
        self.assertNotContains(response, "Another User Task")  

    def test_get_edittask(self):
        # Test user can view the edittask page
        response = self.client.get(reverse('edittask', kwargs={'task_id': self.task.pk}))  
        self.assertContains(response, "User Task")

    def test_post_edittask(self):
        # Test that the user can edit their own task
        response = self.client.post(reverse('edittask', kwargs={'task_id': self.task.pk}), {
            'title': 'Updated Task Title',
            'description': 'Updated description',
            'priority': Task.Priority.HIGH,
            'status': Task.Status.IN_PROGRESS,
            'completed': False
        })
        # Check for a redirect after successful edit
        self.assertEqual(response.status_code, 302)  
        self.task.refresh_from_db()
        # Confirm task was updated
        self.assertEqual(self.task.title, 'Updated Task Title')  

    def test_forbidden_post_edittask(self):
        # Test that a user cannot edit another user's task
        response = self.client.post(reverse('edittask', kwargs={'task_id': self.other_task.pk}), {
            'title': 'Hacked Task Title',
            'description': 'Hacked description',
            'priority': Task.Priority.LOW,
            'status': Task.Status.DONE,
            'completed': True
        })
        # looking for a forbidden response
        self.assertEqual(response.status_code, 403)  

    def test_deletetask(self):
        # Test user can delete their own task
        response = self.client.post(reverse('deletetask', kwargs={'task_id': self.task.pk})) 
        # Check for a redirect after deletion
        self.assertEqual(response.status_code, 302)  
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(pk=self.task.pk)  

    def test_forbidden_deletetask(self):
        # Test that a user cannot delete another user's task
        response = self.client.post(reverse('deletetask', kwargs={'task_id': self.other_task.pk})) 
        # looking for a forbidden response
        self.assertEqual(response.status_code, 403)  