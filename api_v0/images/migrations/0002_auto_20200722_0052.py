# Generated by Django 3.0.8 on 2020-07-22 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='descriptor',
            field=models.CharField(max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='images',
            name='image',
            field=models.ImageField(default='unknow image', upload_to='uploads/images/', verbose_name='Загрузить изображение'),
        ),
    ]
