from django import forms
from django.forms import ModelForm
from .models import Task

class TaskAddForm(forms.ModelForm):
    
    # title = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Task Name'}))
    
    class Meta:
        model = Task
        fields = ['title']
        # Remove the label as placeholder details the input required
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Task Name'})
        }
        
        labels = {
            'title': '',
        }

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status', 'completed']
        labels = ""
        # fields = "__all__"