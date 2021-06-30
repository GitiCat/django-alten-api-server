from django.db import models
from tinymce import models as tinymce_models
from ..files.models import File

class Document(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название документа', max_length=100, null=False)
    title = models.CharField('Заголовок документа', max_length=100, null=False)
    subtitle = models.CharField('Подзаголовок документа', max_length=255, null=True, blank=True)
    category = models.ForeignKey('CategoryDocuments', verbose_name='Категория', on_delete=models.SET_NULL, null=True, blank=True)
    text = tinymce_models.HTMLField('Описание')
    file = models.ForeignKey(File, verbose_name='Файл', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'documents'
        ordering = ['-created_at']
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        managed = True

class CategoryDocuments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название категории документов', max_length=100, null=False)
    title = models.CharField('Заголовок', max_length=100, null=False)
    descriptor = models.CharField('Описание', max_length=255, null=True, blank=True)
    root_category = models.ForeignKey('self', verbose_name='Родительская категория', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'category_documents'
        ordering = ['-created_at']
        verbose_name = 'Категория документов'
        verbose_name_plural = 'Категории документов'
        managed = True