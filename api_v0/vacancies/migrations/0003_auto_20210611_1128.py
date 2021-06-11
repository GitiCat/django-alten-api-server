# Generated by Django 3.1 on 2021-06-11 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_auto_20210610_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancies',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='vacancies',
            name='wage',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заработная плата'),
        ),
    ]