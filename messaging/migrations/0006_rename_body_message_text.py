# Generated by Django 5.0.4 on 2024-04-13 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0005_rename_text_message_body_message_recipient_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='body',
            new_name='text',
        ),
    ]
