from django.db import models

class ListFiles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название списка', max_length=100, null=False)
    descriptor = models.CharField('Описание', max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'list_files'
        ordering = ['-created_at']
        verbose_name = 'Список файлов'
        verbose_name_plural = 'Списки файлов'
        managed = True

class File(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField('Загрузить документ', upload_to='uploads/files', null=False, blank=False)
    descriptor = models.CharField('Описание', max_length=255, null=True, blank=True)
    list_files = models.ForeignKey(ListFiles, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.file.name

    class Meta:
        db_table = 'files'
        ordering = ['-created_at']
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        managed = True