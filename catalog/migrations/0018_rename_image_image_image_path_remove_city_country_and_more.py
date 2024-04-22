# Generated by Django 5.0.4 on 2024-04-18 00:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_alter_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='image_path',
        ),
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.RemoveField(
            model_name='city',
            name='state',
        ),
        migrations.RemoveField(
            model_name='item',
            name='city',
        ),
        migrations.RemoveField(
            model_name='state',
            name='country',
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.city')),
                ('country', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.country')),
                ('state', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.state')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='location',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.location'),
        ),
    ]
