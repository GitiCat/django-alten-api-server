# Generated by Django 3.0.8 on 2020-07-22 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0008_auto_20200722_0130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'managed': True, 'ordering': ['-created_at'], 'verbose_name': 'Галерея', 'verbose_name_plural': 'Галереи'},
        ),
        migrations.AlterField(
            model_name='gallery',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]