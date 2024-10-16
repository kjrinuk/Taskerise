from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib.auth import views as auth_views
# 
#from .views import TaskDetailView


urlpatterns = [
    #
    #path('edittask/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    # Home page path
    path('', include('tasks.urls')),
    path("accounts/", include("allauth.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='/templates/account/login.html'), name='login'),
] + debug_toolbar_urls()
