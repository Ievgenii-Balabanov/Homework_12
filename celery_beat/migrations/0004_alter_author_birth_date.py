# Generated by Django 4.0 on 2023-07-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celery_beat', '0003_rename_city_author_hometown_remove_author_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.CharField(max_length=70),
        ),
    ]
