# Generated by Django 5.1.7 on 2025-03-30 20:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('vehicle_plate', models.CharField(max_length=7)),
                ('checkin_datetime', models.DateTimeField(auto_now=True)),
                ('parked', models.BooleanField(default=False)),
                ('driver', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='driver.driver')),
            ],
        ),
    ]
