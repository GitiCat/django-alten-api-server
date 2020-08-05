# Generated by Django 3.0.8 on 2020-08-05 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0011_auto_20200722_1602'),
        ('article', '0005_article_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='main_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='images.Images', verbose_name='Основное изображение'),
        ),
        migrations.AlterField(
            model_name='categoryarticle',
            name='descriptor',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
    ]
