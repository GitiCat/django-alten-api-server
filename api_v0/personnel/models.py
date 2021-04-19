from django.db import models
from tinymce import models as tinymce_models

class CommunicationMethod(models.Model):
    id = models.AutoField(primary_key=True)
    is_visible = models.BooleanField('Отображение данных связи', default=True)
    name = models.CharField('Название', max_length=256, null=False, blank=False)
    descriptor = tinymce_models.HTMLField(verbose_name='Описание', null=True, blank=True)
    responsible = models.CharField('Ответственный', max_length=256, null=True, blank=True)
    position = models.CharField('Должность', max_length=100, null=True, blank=True)
    phone = models.CharField('Телефон', max_length=30, null=True, blank=True)
    is_phone_visible = models.BooleanField('Отображение номера телефона', default=True)
    fax = models.CharField('Факс / телефон', max_length=30, null=True, blank=True)
    is_fax_visible = models.BooleanField('Отображение номера факса', default=True)
    email = models.CharField('Электронная почта', max_length=100, null=True, blank=True)
    is_email_visible = models.BooleanField('Отображение электронной почты', default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'communication_methods'
        ordering = ['-created_at']
        verbose_name = 'Метод связи'
        verbose_name_plural = 'Методы связи'
        managed = True

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=256, null=False)
    descriptor = tinymce_models.HTMLField(verbose_name="Описание", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

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
    department = models.ForeignKey(Department, verbose_name="Подразделение", on_delete=models.SET_NULL, null=True, blank=False)
    communication_method = models.ForeignKey(CommunicationMethod, verbose_name='Метод связи', on_delete=models.SET_NULL, null=True, blank=False)
    phone = models.CharField(verbose_name="Телефон", max_length=30, null=True, blank=True)
    is_phone_visible = models.BooleanField('Отображение номера телефона', default=True)
    email = models.CharField(verbose_name="Электронная почта", max_length=100, null=True, blank=True)
    is_email_visible = models.BooleanField('Отображение электронной почты', default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'personnel'
        ordering = ['-created_at']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Персонал'
        managed = True