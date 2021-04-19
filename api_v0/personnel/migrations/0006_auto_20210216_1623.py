# Generated by Django 3.1 on 2021-02-16 13:23

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0005_auto_20210215_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='department',
            name='descriptor',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]