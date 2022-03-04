# Generated by Django 4.0.2 on 2022-03-02 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreA', models.CharField(max_length=200)),
                ('apellidoA', models.CharField(max_length=200)),
                ('DescripciónA', models.CharField(max_length=1000)),
                ('fotoA', models.CharField(default='link', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Obras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('sinopsis', models.CharField(max_length=1000)),
                ('foto', models.CharField(default='link', max_length=200)),
                ('duración', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=200)),
                ('publico', models.CharField(max_length=200)),
                ('cant_actores', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Personajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrep', models.CharField(max_length=200)),
                ('Descripción', models.CharField(max_length=11000)),
                ('fotoP', models.CharField(default='link', max_length=200)),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.obras')),
            ],
        ),
    ]
