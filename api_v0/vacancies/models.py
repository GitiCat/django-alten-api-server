from django.db import models
from tinymce import models as tinymce_models

class Employment(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='Заголовок', max_length=50, null=False, blank=False)
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'employment'
        ordering = ['-created_at']
        verbose_name = 'Вид занятости'
        verbose_name_plural = 'Виды занятости'
        managed = True

class Vacancies(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Название', max_length=100, null=False, blank=False)
    title = models.CharField(verbose_name='Заголовок', max_length=100, null=False, blank=False)
    wage = models.CharField(verbose_name='Заработная плата', max_length=255, null=True, blank=True)
    city = models.CharField(verbose_name='Город', max_length=100, null=True, blank=False)
    employment = models.ForeignKey(Employment, verbose_name='Вид занятости', on_delete=models.SET_NULL, null=True, blank=True)
    requirements = tinymce_models.HTMLField(verbose_name='Требования', null=True, blank=True)
    descriptor = tinymce_models.HTMLField(verbose_name='Описание вакансии', null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Активность вакансии', default=True)
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'vacancies'
        ordering = ['-created_at']
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        managed = True