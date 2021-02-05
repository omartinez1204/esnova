# Generated by Django 3.1.2 on 2021-02-05 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosapp', '0032_subirarchivos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gastofamiliarmensual',
            name='otros_1',
        ),
        migrations.RemoveField(
            model_name='gastofamiliarmensual',
            name='otros_2',
        ),
        migrations.AddField(
            model_name='gastofamiliarmensual',
            name='nombre_gasto_1',
            field=models.CharField(default='cualquier gasto', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gastofamiliarmensual',
            name='nombre_gasto_2',
            field=models.CharField(default='cualquiera', max_length=100),
            preserve_default=False,
        ),
    ]
