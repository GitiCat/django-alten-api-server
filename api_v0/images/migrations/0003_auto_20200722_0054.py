# Generated by Django 3.0.8 on 2020-07-22 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20200722_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='descriptor',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
    ]
