# Generated by Django 5.0.4 on 2024-04-13 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_category_name_alter_city_name_alter_city_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='catalog/static/img/%Y/%m/%d/', verbose_name='Path to image'),
        ),
    ]
