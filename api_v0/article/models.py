from django.db import models
from tinymce import models as tinymce_models
from ..images.models import Images

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название статьи', max_length=100, null=False)
    title = models.CharField('Заголовок', max_length=155, null=False)
    subtitle = models.CharField('Подзаголовок', max_length=255, null=True, blank=True)
    category = models.ForeignKey('CategoryArticle', verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    text = tinymce_models.HTMLField()
    main_image = models.ForeignKey(Images, verbose_name='Основное изображение', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'article'
        ordering = ['-created_at']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        managed = True


class CategoryArticle(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название категории статей', max_length=100, null=False)
    title = models.CharField('Заговок', max_length=100, default='', blank=True)
    descriptor = models.CharField('Описание', max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category_article'
        ordering = ['-created_at']
        verbose_name = 'Категория статей'
        verbose_name_plural = 'Категории статей'
        managed = True