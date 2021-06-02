from django.db import models
from tinymce import models as tinymce_models
from ..images.models import Images
from ..files.models import File

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название продукта', max_length=100, null=False, blank=False)
    title = models.CharField('Заголовок продукта', max_length=255, null=False, blank=False)
    category = models.ForeignKey('CategoryProduct', verbose_name='Категория', on_delete=models.SET_NULL, null=True, blank=False)
    descriptor = tinymce_models.HTMLField(verbose_name='Описание', null=True, blank=True)
    feature = tinymce_models.HTMLField(verbose_name='Характеристики', null=True, blank=True)
    main_image = models.ForeignKey(Images, verbose_name='Основное изображение', on_delete=models.SET_NULL, null=True, blank=True)
    file = models.ForeignKey(File, verbose_name='Файл для загрузки', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        managed = True

class CategoryProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название категории продукции', max_length=100, null=False, blank=False)
    title = models.CharField('Заголовок категории', max_length=255, null=False, blank=False)
    descriptor = tinymce_models.HTMLField(verbose_name='Описание категории', null=True, blank=True)
    sub_descriptor = tinymce_models.HTMLField(verbose_name='Дополнительное описание категории', null=True, blank=True)
    preview_image = models.ForeignKey(Images, verbose_name='Изображение', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category_product'
        ordering = ['-created_at']
        verbose_name = 'Категория продукции'
        verbose_name_plural = 'Категории продукции'
        managed = True