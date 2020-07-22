from django.db import models
from tinymce import models as tinymce_models
from ..images.models import Gallery

class News(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название новости', max_length=100, null=False)
    title = models.CharField('Заголовок', max_length=155, null=False)
    subtitle = models.CharField('Подзаголовок', max_length=255, null=True, blank=True)
    text = tinymce_models.HTMLField('Текст новости')
    main_image = models.ImageField('Основное изображение', upload_to='uploads/images/', null=True, blank=True)
    gallery = models.ForeignKey(Gallery, verbose_name='Галерея', on_delete=models.SET_NULL, null=True, blank=True)
    original_url = models.URLField('Ссылка на оригинал', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'news'
        ordering = ['-created_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        managed = True