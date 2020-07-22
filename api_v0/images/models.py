from django.db import models

class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=100, null=False, blank=False)
    descriptor = models.CharField('Описание', max_length=255, blank=True, default='no description...')
    head_image = models.ImageField('Изображение галереи', upload_to='uploads/gallery/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Gallery'
        ordering = ['-created_at']
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'
        managed = True

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField('Загрузить изображение', upload_to='uploads/images/', null=False, blank=False)
    descriptor = models.CharField('Описание', max_length=255, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name

    class Meta:
        db_table = 'images'
        ordering = ['-created_at']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        managed = True