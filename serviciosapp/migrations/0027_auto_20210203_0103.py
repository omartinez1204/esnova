# Generated by Django 3.1.2 on 2021-02-03 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosapp', '0026_auto_20210202_0158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingresofamiliarmensual',
            old_name='usuario_fore',
            new_name='usuario_foraneo',
        ),
    ]