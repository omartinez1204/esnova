# Generated by Django 3.1.2 on 2021-02-01 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosapp', '0006_auto_20210131_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingresofamiliarmensual',
            name='apoyo_F_E',
            field=models.CharField(max_length=3),
        ),
    ]
