# Generated by Django 5.0.3 on 2024-03-16 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_person'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='delete_at',
            new_name='deleted_at',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]