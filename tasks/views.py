from django.shortcuts import render
from django.views import generic
from .models import Task

# edittask request
from django.http import HttpResponse
from django.template import loader


# Create your views here.
class TaskList(generic.ListView):
    queryset = Task.objects.filter()
    template_name = "tasks/index.html"
    # paginate_by = 12

def edittask(request):
    template = loader.get_template('tasks/edittask.html')
    return HttpResponse(template.render())
    