from django.db import models
from tinymce import models as tinymce_models
from ..images.models import Images, Gallery

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название продукта', max_length=100, null=False, blank=False)
    title = models.CharField('Заголовок продукта', max_length=255, null=False, blank=False)
    category = models.ForeignKey('CategoryProduct', verbose_name='Категория', on_delete=models.SET_NULL, null=True, blank=False)
    descriptor = tinymce_models.HTMLField(verbose_name='Описание')
    main_image = models.ForeignKey(Images, verbose_name='Основное изображение', on_delete=models.SET_DEFAULT, null=False, blank=False, default='media/uploads/images/default.png')
    
    created_at = models.DateTimeField(auto_now_add=True)

class CategoryProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название категории продукции', max_length=100, null=False, blank=False)
    title = models.CharField('Заголовок категории', max_length=255, null=False, blank=False)
    descriptor = tinymce_models.HTMLField(verbose_name='Описание категории' null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category_product'
        ordering = ['-created_at']
        verbose_name = 'Категория продукции'
        verbose_name_plural = 'Категории продукции'
        managed = True