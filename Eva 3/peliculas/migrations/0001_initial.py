# Generated by Django 4.2.7 on 2023-11-20 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pelicula', models.CharField(max_length=100)),
                ('duracion_pelicula', models.DurationField()),
                ('fecha_estreno', models.DateField()),
                ('genero', models.CharField(max_length=50)),
                ('clasificacion', models.CharField(max_length=10)),
                ('tipo_pelicula', models.CharField(max_length=10)),
            ],
        ),
    ]
