# Generated by Django 3.0.8 on 2020-07-21 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('extension', models.CharField(max_length=10, verbose_name='Расширение')),
                ('size', models.DecimalField(decimal_places=1, max_digits=7, verbose_name='Размер')),
                ('path', models.CharField(max_length=255, verbose_name='Путь')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
                'db_table': 'images',
                'ordering': ['-created_at'],
                'managed': True,
            },
        ),
    ]
