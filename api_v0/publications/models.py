from django.db import models
from tinymce import models as tinymce_models
from ..images.models import Images
from ..files.models import ListFiles

class CategoryPublication(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Название категории', max_length=100, null=False, blank=False)
    descriptor = tinymce_models.HTMLField(verbose_name='Описание категории', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories_publicatio'
        ordering = ['-created_at']
        verbose_name = 'Категория публикации'
        verbose_name_plural = 'Категории публикаций'
        managed = True

class Publication(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(CategoryPublication, verbose_name='Категория', on_delete=models.CASCADE, null=True, blank=False)
    name = models.CharField('Название публикации', max_length=100, null=False, blank=False)
    title = models.CharField('Заголовок публикации', max_length=255, null=False, blank=False)
    subtitle = models.CharField('Подзаголовок публикации', max_length=255, null=True, blank=True)
    descriptor = tinymce_models.HTMLField(verbose_name='Описание', null=True, blank=True)
    main_image = models.ForeignKey(Images, verbose_name='Основное изображение', on_delete=models.CASCADE, null=True, blank=True)
    files = models.ForeignKey(ListFiles, verbose_name='Файлы', on_delete=models.SET_NULL, null=True, blank=True)
    url = models.CharField('Ссылка на публикацию', max_length=1000, null=True, blank=True)
    is_active = models.BooleanField('Автивность статьи', default=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publications'
        ordering = ['-created_at']
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        managed = True