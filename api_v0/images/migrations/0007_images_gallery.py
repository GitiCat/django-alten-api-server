# Generated by Django 3.0.8 on 2020-07-22 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0006_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='gallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='images.Gallery'),
        ),
    ]