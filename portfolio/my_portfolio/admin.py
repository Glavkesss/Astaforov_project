from django.contrib import admin
from .models import Project
from users.models import User
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price']
    list_editable = ['price']

admin.site.register(Project, ProjectAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone_number', 'instagram', 'facebook']

admin.site.register(User, UserAdmin)