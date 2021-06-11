from django.contrib import admin

from .models import Vacancies, Employment

@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at')
    
@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')