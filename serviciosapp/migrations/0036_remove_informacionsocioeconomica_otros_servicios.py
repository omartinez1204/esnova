# Generated by Django 3.1.2 on 2021-02-08 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosapp', '0035_auto_20210206_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informacionsocioeconomica',
            name='otros_servicios',
        ),
    ]
