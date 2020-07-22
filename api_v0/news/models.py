from django.db import models
from tinymce import models as tinymce_models

class News(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название новости', max_length=100, null=False)
    title = models.CharField('Заголовок', max_length=155, null=False)
    subtitle = models.CharField('Подзаголовок', max_length=255, null=True)
    category = models.ForeignKey('CategoryNews', on_delete=models.SET_DEFAULT, default='unknow category...')
    text = tinymce_models.HTMLField()
    main_image = models.ImageField('Основное изображение', upload_to='uploads/images/')
    gallery = models.F
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'news'
        ordering = ['-created_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        managed = True