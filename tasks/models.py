from django.db import models
from django.contrib.auth.models import User

PRIORITIES = (
    (1, "Low")
    (2, "Medium")
    (3, "High")    
    (4, "Urgent")
)


# Create your models here.
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    due_date = models.DateField()
    # Add due_time to next development phase
    #due_time = models.TimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # Foreign keys for relationships with other database files
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    # Maybe create a priority tuple (P1, P2, P3, P4) to choose from and default to P4 
    priority = models.IntegerField(Priority, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    # Add Project and category in next development phase
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # project = models.ForeignKey(Project, on_delete=models.CASCADE)
