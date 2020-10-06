# Generated by Django 3.1 on 2020-10-06 12:50

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0011_auto_20200722_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Название публикации')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок публикации')),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Подзаголовок публикации')),
                ('descriptor', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Описание')),
                ('url', models.TextField(blank=True, null=True, verbose_name='Ссылка на публикацию')),
                ('is_active', models.BooleanField(default=True, verbose_name='Автивность статьи')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('main_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='images.images', verbose_name='Основное изображение')),
            ],
            options={
                'verbose_name': ('Публикация',),
                'verbose_name_plural': 'Публикации',
                'db_table': 'publications',
                'ordering': ['-created_at'],
                'managed': True,
            },
        ),
    ]
