# Generated by Django 5.1.7 on 2025-04-01 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0004_alter_driver_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='driver_docs/'),
        ),
    ]
