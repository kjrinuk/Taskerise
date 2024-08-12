from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .models import Task
from .forms import TaskForm


# Create your views here.
class TaskList(generic.ListView):
    queryset = Task.objects.filter()
    template_name = "tasks/index.html"
    # paginate_by = 12

def index(request): 

    form = TaskForm()
    tasks = Task.objects.all()
 
    context = {'tasks': tasks, 'TaskForm': form}

    return render(request, "tasks/tasks.html", context)

def edittask(request, task_id):
    # Call form
    #taskform = TaskForm()
    task = get_object_or_404(Task, task_id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the task list page after saving
    else:
        form = TaskForm(instance=task)
    
    context = {'form': form, 'task': task}    

    return render(request, "tasks/edittask.html", context)
    
   
    