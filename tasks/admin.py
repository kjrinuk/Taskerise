from django.contrib import admin
from .models import Task
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# admin.site.register(Task)
@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):

    list_display = ('title', 'due_date', 'priority', 'status')
    search_fields = ['title']
    list_filter = ('priority',)
    #prepopulated_fields = {'due_date': ('title',)}
    summernote_fields = ('description',)