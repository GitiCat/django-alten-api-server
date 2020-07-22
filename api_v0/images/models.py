from django.db import models

class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название альбома', max_length=100, null=False, blank=False)
    descriptor = models.CharField('Описание', max_length=255, blank=True, default='no description...')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Gallery'
        ordering = ['-created_at']
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        managed = True

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField('Загрузить изображение', upload_to='uploads/images/', default='unknow image', blank=False)
    descriptor = models.CharField('Описание', max_length=255, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name

    class Meta:
        db_table = 'images'
        ordering = ['-created_at']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        managed = True