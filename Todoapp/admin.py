from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    search_fields=['task']
    list_display = ('id', 'task', 'is_completed', 'created_at')
admin.site.register(Task,TaskAdmin)
