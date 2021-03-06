# Generated by Django 3.1 on 2021-02-15 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0003_auto_20210215_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personnel.department', verbose_name='Подразделение'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Телефон'),
        ),
    ]
