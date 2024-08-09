from tasks import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [   
    path('', views.TaskList.as_view(), name='home'),
    path('edittask', views.edittask, name='edittask'),
]