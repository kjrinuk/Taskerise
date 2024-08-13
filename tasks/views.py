from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .models import Task
from .forms import TaskForm, TaskAddForm


# Create your views here.
# class TaskList(generic.ListView):
#     queryset = Task.objects.filter()
#     template_name = "tasks/index.html"
  
# Function to Add a task
def index(request): 
    # Only show tasks for logged in user
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
    else:
        tasks=Task.objects.none()

    
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

# Function to delete a chosen task
def deleteTask(request, task_id):
    task = Task.objects.get(task_id = task_id)

    if request.method == 'POST':
            task.delete()

            return redirect('/')

    context = {'task': task}

    return render(request, 'tasks/deletetask.html', context)

# Function to edit a chose task
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
    
   
    