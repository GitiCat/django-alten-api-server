from django.db import models

class EmailModel(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField('Имя', max_length=254, null=False, blank=False)
    email = models.EmailField('Электронная почта', null=False, blank=False)
    phone = models.CharField('Номер телефона', max_length=25, null=False, blank=False)
    message = models.TextField('Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.full_name

    class Meta:
        db_table: 'emails'
        ordering = ['-created_at']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        managed = True