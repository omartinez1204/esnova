# Generated by Django 3.1.2 on 2021-01-25 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosapp', '0002_auto_20210121_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=30)),
                ('contrasenia', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='residencia_distinta',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='solicita_beca_alimentaria',
            field=models.CharField(max_length=3),
        ),
    ]
