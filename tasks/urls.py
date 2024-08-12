from . import views
from django.urls import path, include
from django.views.generic import TemplateView
from .views import edittask, index

urlpatterns = [   
    # path('', views.TaskList.as_view(), name='home'),
    path('', index, name = 'index'),
    # path('addtask', views.addtask, name='addtask'),
    path('edittask/<int:task_id>/', views.edittask, name='edittask'),
    path('deletetask/<int:task_id>/', views.deleteTask, name='deletetask'),
]