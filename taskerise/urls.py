from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    # Home page path
    path('', include('tasks.urls')),
    path("accounts/", include("allauth.urls")),
 
] + debug_toolbar_urls()
