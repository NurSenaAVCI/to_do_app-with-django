from django.contrib import admin
from .models import * 

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'complate', 'created')

admin.site.register(Task, TaskAdmin)


# Register your models here.
