# Generated by Django 3.1.3 on 2021-02-05 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosapp', '0031_auto_20210204_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='subirArchivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('media', models.FileField(blank=True, null=True, upload_to='myfolder/')),
            ],
        ),
    ]
