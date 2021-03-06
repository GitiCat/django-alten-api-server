# Generated by Django 3.0.8 on 2020-07-28 10:39

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryArticle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Название категории статей')),
                ('title', models.CharField(blank=True, default='', max_length=100, verbose_name='Заговок')),
                ('descriptor', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Категория статей',
                'verbose_name_plural': 'Категории статей',
                'db_table': 'category_article',
                'ordering': ['-created_at'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Название статьи')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовок')),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Подзаголовок')),
                ('text', tinymce.models.HTMLField()),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='uploads/images/', verbose_name='Основное изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.CategoryArticle', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'db_table': 'article',
                'ordering': ['-created_at'],
                'managed': True,
            },
        ),
    ]
