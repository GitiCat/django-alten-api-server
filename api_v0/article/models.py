from django.db import models
from tinymce import models as tinymce_models

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название статьи', max_length=100, null=False)
    title = models.CharField('Заголовок', max_length=155, null=False)
    subtitle = models.CharField('Подзаголовок', max_length=255, null=True, blank=True)
    category = models.ForeignKey('CategoryArticle', on_delete=models.SET_DEFAULT, null=True, default='unknow category...')
    text = tinymce_models.HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)

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
    descriptor = tinymce_models.HTMLField('Описание', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category_article'
        ordering = ['-created_at']
        verbose_name = 'Категория статей'
        verbose_name_plural = 'Категории статей'
        managed = True