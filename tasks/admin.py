from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Task

# Register your models here.
# admin.site.register(Task)
@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):

    list_display = ('title', 'due_date', 'priority', 'status')
    search_fields = ['title']
    list_filter = ('priority', 'status', 'due_date')
    summernote_fields = ('description',)