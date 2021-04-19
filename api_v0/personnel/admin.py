from django.contrib import admin
from .models import Department, Personnel, CommunicationMethod

@admin.register(CommunicationMethod)
class CommunicationMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')

@admin.register(Department)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')


@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')