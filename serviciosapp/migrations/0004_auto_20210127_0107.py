# Generated by Django 3.1.2 on 2021-01-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosapp', '0003_auto_20210124_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datospersonadequiendepende',
            name='dependencia_jubilo',
        ),
        migrations.RemoveField(
            model_name='datospersonadequiendepende',
            name='jubilado',
        ),
        migrations.RemoveField(
            model_name='datospersonadequiendepende',
            name='labores_del_campo',
        ),
        migrations.RemoveField(
            model_name='datospersonadequiendepende',
            name='negocio_propio',
        ),
        migrations.RemoveField(
            model_name='datospersonadequiendepende',
            name='tipo_de_producto',
        ),
        migrations.AddField(
            model_name='datospersonadequiendepende',
            name='texto_ocupacion',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='datospersonadequiendepende',
            name='calle',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='datospersonadequiendepende',
            name='ocupacion',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='datospersonadequiendepende',
            name='sexo',
            field=models.CharField(max_length=30),
        ),
    ]
