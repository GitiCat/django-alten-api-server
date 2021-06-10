from django.contrib import admin

from .models import Vacancies

@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at')