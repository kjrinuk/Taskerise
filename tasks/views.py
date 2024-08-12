from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .models import Task
from .forms import TaskForm, TaskAddForm


# Create your views here.
# class TaskList(generic.ListView):
#     queryset = Task.objects.filter()
#     template_name = "tasks/index.html"
  

def index(request): 
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskAddForm(request.POST)
        if form.is_valid():
            form.save()
            print("form is valid")
            return redirect('/')
    else:
        form = TaskAddForm()
    
    context = {'tasks': tasks, 'TaskAddForm': form}
    return render(request, "tasks/tasks.html", context)

# def addtask(request)

#     task = get_object_or_404(Task)

#     return render(request, 'tasks/add_task.html')

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
    
   
    