from django.shortcuts import render
from django.views import generic
from .models import Task


# Create your views here.
class TaskList(generic.ListView):
    queryset = Task.objects.filter()
    template_name = "tasks/tasklist.html"
    # model = Task