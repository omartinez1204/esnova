# Generated by Django 3.1.2 on 2021-02-01 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosapp', '0005_auto_20210131_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosdelresponsable',
            name='usuario_fore',
        ),
        migrations.RemoveField(
            model_name='datospersonadequiendepende',
            name='usuario_fore',
        ),
        migrations.RemoveField(
            model_name='datospersonales',
            name='usuario_fore',
        ),
        migrations.RemoveField(
            model_name='gastofamiliarmensual',
            name='usuario_fore',
        ),
        migrations.RemoveField(
            model_name='gastosdelsolicitante',
            name='usuario_fore',
        ),
        migrations.RemoveField(
            model_name='informacionsocioeconomica',
            name='usuario_fore',
        ),
        migrations.RemoveField(
            model_name='ingresofamiliarmensual',
            name='usuario_fore',
        ),
        migrations.RemoveField(
            model_name='mediosparaestudiar',
            name='usuario_fore',
        ),
        migrations.RemoveField(
            model_name='personasquedependendelingresomensual',
            name='usuario_fore',
        ),
    ]
