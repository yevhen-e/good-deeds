# Generated by Django 5.0.4 on 2024-04-18 00:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_rename_image_image_image_path_remove_city_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='location',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.country'),
        ),
    ]