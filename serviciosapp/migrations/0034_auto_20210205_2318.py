# Generated by Django 3.1.2 on 2021-02-06 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosapp', '0033_auto_20210205_0153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informacionsocioeconomica',
            old_name='servicios_publicos',
            new_name='otro_servicio',
        ),
        migrations.RemoveField(
            model_name='informacionsocioeconomica',
            name='casa_cuenta_con',
        ),
        migrations.RemoveField(
            model_name='informacionsocioeconomica',
            name='servicios_vivienda',
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='agua',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='aire_acondicionado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='alumbrado_publico',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='aspiradora',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='calentador_de_gas',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='computadora_de_escritorio',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='drenaje',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='drenaje_publico',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='dvd',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='equipo_de_sonido',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='estufa_de_gas',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='laptop',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='lavadora',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='luz',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='microondas',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='otro_servicio_vivienda',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='pavimentacion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='podadora',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='refrigerador',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='telefono',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='television_por_cable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='televisor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='videocamara',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informacionsocioeconomica',
            name='videojuegos',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='informacionsocioeconomica',
            name='apoyo_dependencia',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='informacionsocioeconomica',
            name='automovil',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='informacionsocioeconomica',
            name='biblioteca',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='informacionsocioeconomica',
            name='cochera',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='informacionsocioeconomica',
            name='comedor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='informacionsocioeconomica',
            name='cuarto_estudio',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='informacionsocioeconomica',
            name='cuarto_servicio',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='informacionsocioeconomica',
            name='monto_apoyo',
            field=models.FloatField(default=False),
        ),
        migrations.AlterField(
            model_name='informacionsocioeconomica',
            name='patio',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='informacionsocioeconomica',
            name='sala',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='informacionsocioeconomica',
            name='terraza',
            field=models.BooleanField(default=False),
        ),
    ]
