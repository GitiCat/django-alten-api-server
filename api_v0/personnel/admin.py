from django.contrib import admin
from .models import Department, Personnel

@admin.register(Department)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')


@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')