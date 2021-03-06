# Generated by Django 3.1.2 on 2021-02-14 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosapp', '0036_remove_informacionsocioeconomica_otros_servicios'),
    ]

    operations = [
        migrations.AddField(
            model_name='subirarchivos',
            name='usuario_fore',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='serviciosapp.usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subirarchivos',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='%Y/%m/%d/'),
        ),
    ]
