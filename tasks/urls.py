from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import TemplateView
from .views import edittask, index
from . import views

urlpatterns = [   
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', index, name = 'index'),
    path('edittask/<int:task_id>/', views.edittask, name='edittask'),
    path('deletetask/<int:task_id>/', views.deleteTask, name='deletetask'),
]