from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    # set values for Priorities
    class Priority(models.IntegerChoices):
        LOW = 1, 'Low'
        MEDIUM = 2, 'Medium'
        HIGH = 3, 'High'
        URGENT = 4, 'Urgent'
    
    # set values for the Status
    class Status(models.IntegerChoices):
        TO_DO = 1, 'To Do'
        IN_PROGRESS = 2, 'In Progress'
        DONE = 3, 'Done'
    
    # Create task model
    # although task_id is automatically assigned i've added it for my sake only
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    due_date = models.DateField()
    # Add due_time to next development phase
    #due_time = models.TimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    # Foreign keys for relationships with other database files
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Set priority and status using choices set in classes above
    priority = models.IntegerField(choices=Priority.choices, default=Priority.LOW)
    status = models.IntegerField(choices=Status.choices, default=Status.TO_DO)
    
    completed = models.BooleanField(default=False)
    #####################################################################
    # Add Project and category in next development phase                #
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)  #
    # project = models.ForeignKey(Project, on_delete=models.CASCADE)    #
    #####################################################################