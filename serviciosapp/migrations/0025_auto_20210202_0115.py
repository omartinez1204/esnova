# Generated by Django 3.1.2 on 2021-02-02 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosapp', '0024_auto_20210202_0112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datospersonadequiendepende',
            old_name='usuario_fore',
            new_name='usuario_foraneo',
        ),
    ]
