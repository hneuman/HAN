# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0002_persona_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buzon_entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_persona', models.CharField(max_length=100)),
                ('numero_telefono', models.CharField(max_length=100)),
                ('grupo_asociado', models.CharField(max_length=100)),
                ('contenido_mensaje', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Buzon_enviados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_persona', models.CharField(max_length=100)),
                ('numero_telefono', models.CharField(max_length=100)),
                ('grupo_asociado', models.CharField(max_length=100)),
                ('contenido_mensaje', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Buzon_pendientes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_persona', models.CharField(max_length=100)),
                ('numero_telefono', models.CharField(max_length=100)),
                ('grupo_asociado', models.CharField(max_length=100)),
                ('contenido_mensaje', models.CharField(max_length=100)),
            ],
        ),
    ]
