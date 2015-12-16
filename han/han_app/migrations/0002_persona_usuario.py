# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_persona', models.CharField(max_length=100)),
                ('cedula_persona', models.CharField(max_length=100)),
                ('numero_telefono', models.CharField(max_length=100)),
                ('grupo_asociado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(default=b'Sin Nombre', max_length=100)),
                ('cedula', models.CharField(default=b'0000000', max_length=100)),
                ('direccion', models.TextField(default=b'-----------------')),
                ('codigo_u', models.CharField(default=b'no Codigo', max_length=100)),
                ('telefono', models.CharField(default=b'No Telefono', max_length=100)),
                ('email', models.CharField(default=b'No Email', max_length=100)),
                ('genero', models.CharField(default=b'No Genero', max_length=100)),
                ('fecha_nacimiento', models.DateField(auto_now=True)),
                ('nacionalidad', models.CharField(default=b'V', max_length=20)),
                ('grupo_asociado', models.CharField(default=b'sin grupo', max_length=100)),
            ],
        ),
    ]
