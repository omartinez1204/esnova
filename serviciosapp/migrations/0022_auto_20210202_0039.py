# Generated by Django 3.1.2 on 2021-02-02 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosapp', '0021_auto_20210202_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosdelresponsable',
            name='usuario_fore',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='serviciosapp.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datospersonadequiendepende',
            name='usuario_fore',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='serviciosapp.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gastofamiliarmensual',
            name='usuario_fore',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='serviciosapp.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gastosdelsolicitante',
            name='usuario_fore',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='serviciosapp.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='usuario_fore',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='serviciosapp.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingresofamiliarmensual',
            name='usuario_fore',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='serviciosapp.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mediosparaestudiar',
            name='usuario_fore',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='serviciosapp.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personasquedependendelingresomensual',
            name='usuario_fore',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='serviciosapp.usuario'),
            preserve_default=False,
        ),
    ]
