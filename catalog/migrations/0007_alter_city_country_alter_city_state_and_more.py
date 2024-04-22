# Generated by Django 5.0.3 on 2024-04-11 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_rename_stuff_item_rename_stuff_media_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.country'),
        ),
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.state'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='city',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.city'),
        ),
    ]