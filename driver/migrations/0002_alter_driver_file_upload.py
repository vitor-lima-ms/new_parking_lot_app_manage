# Generated by Django 5.1.7 on 2025-04-01 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='driver/uploaded_files'),
        ),
    ]
