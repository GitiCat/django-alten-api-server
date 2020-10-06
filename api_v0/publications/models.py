from django.db import models
from tinymce import models as tinymce_models
from ..images.models import Images

class Publication(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название публикации', max_length=100, null=False, blank=False)
    title = models.CharField('Заголовок публикации', max_length=255, null=False, blank=False)
    subtitle = models.CharField('Подзаголовок публикации', max_length=255, null=True, blank=True)
    descriptor = tinymce_models.HTMLField(verbose_name='Описание', null=True, blank=True)
    main_image = models.ForeignKey(Images, verbose_name='Основное изображение', on_delete=models.CASCADE, null=True, blank=True)
    url = models.CharField('Ссылка на публикацию', max_length=1000, null=True, blank=True)
    is_active = models.BooleanField('Автивность статьи', default=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publications'
        ordering = ['-created_at']
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        managed = True