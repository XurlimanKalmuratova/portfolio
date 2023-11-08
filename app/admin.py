from django.contrib import admin
from .models import *
admin.site.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


