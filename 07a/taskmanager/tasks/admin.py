from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Task._meta.fields]
    list_filter = ('due',)


admin.site.register(Task, TaskAdmin)
