# Generated by Django 3.1 on 2021-06-10 07:09

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Подзаголовок')),
                ('descriptor', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Описание вакансии')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность вакансии')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'db_table': 'vacancies',
                'ordering': ['-created_at'],
                'managed': True,
            },
        ),
    ]