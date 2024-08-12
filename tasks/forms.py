from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(forms.ModelForm):
    
    #title = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Task Name'}))
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status', 'completed']
        labels = ""
        # fields = "__all__"