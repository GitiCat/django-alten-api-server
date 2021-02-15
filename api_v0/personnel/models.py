from django.db import models
from tinymce import models as tinymce_models

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=256, null=False)
    descriptor = tinymce_models.HTMLField();
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'departments'
        ordering = ['-created_at']
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        managed = True

class Personnel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Имя сотрудника", max_length=256, null=False)
    position = models.CharField(verbose_name="Должность", max_length=100, null=False)
    department = models.ForeignKey(Department, verbose_name="Подразделение", on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(verbose_name="Телефон", max_length=30, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'personnel'
        ordering = ['-created_at']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Персонал'
        managed = True