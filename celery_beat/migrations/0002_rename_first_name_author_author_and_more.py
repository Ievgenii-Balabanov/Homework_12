# Generated by Django 4.0 on 2023-07-14 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celery_beat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='first_name',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
    ]