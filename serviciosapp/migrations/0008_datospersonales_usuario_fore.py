# Generated by Django 3.1.2 on 2021-02-02 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosapp', '0007_auto_20210131_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='datospersonales',
            name='usuario_fore',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='serviciosapp.usuario'),
            preserve_default=False,
        ),
    ]
