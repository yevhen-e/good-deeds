# Generated by Django 5.0.4 on 2024-04-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_remove_media_media_path_media_media_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='media_item',
            field=models.ImageField(blank=True, upload_to='static/media/'),
        ),
    ]