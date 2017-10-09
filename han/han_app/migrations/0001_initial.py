# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buzon_entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_persona', models.CharField(max_length=100)),
                ('numero_telefono', models.CharField(max_length=100)),
                ('grupo_asociado', models.CharField(max_length=100)),
                ('contenido_mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Buzon_enviados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_persona', models.CharField(max_length=100)),
                ('numero_telefono', models.CharField(max_length=100)),
                ('grupo_asociado', models.CharField(max_length=100)),
                ('usuario_envia', models.CharField(default=b'', max_length=100)),
                ('contenido_mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Buzon_pendientes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_persona', models.CharField(max_length=100)),
                ('numero_telefono', models.CharField(max_length=100)),
                ('grupo_asociado', models.CharField(max_length=100)),
                ('contenido_mensaje', models.TextField()),
                ('asignado', models.BooleanField(default=False)),
                ('asignado_a', models.CharField(default=b'', max_length=100)),
                ('asignado_hora', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_grupo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_persona', models.CharField(max_length=100)),
                ('cedula_persona', models.CharField(max_length=100)),
                ('numero_telefono', models.CharField(max_length=100)),
                ('grupo_asociado', models.CharField(max_length=100)),
                ('grupo_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(default=b'Sin Nombre', max_length=100)),
                ('cedula', models.CharField(default=b'0000000', max_length=100)),
                ('direccion', models.TextField(default=b'-------------')),
                ('codigo_u', models.CharField(default=b'no Codigo', max_length=100)),
                ('telefono', models.CharField(default=b'No Telefono', max_length=100)),
                ('email', models.CharField(default=b'No Email', max_length=100)),
                ('genero', models.CharField(default=b'No Genero', max_length=100)),
                ('fecha_nacimiento', models.DateField(auto_now=True)),
                ('nacionalidad', models.CharField(default=b'V', max_length=20)),
                ('grupo_asociado', models.CharField(default=b'sin grupo', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_envia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_usuario_envia', models.CharField(max_length=100)),
                ('id_usuario_envia', models.CharField(max_length=100)),
                ('contador', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_historial_mensaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_mensaje', models.CharField(max_length=100)),
                ('numero_telefono', models.CharField(max_length=100)),
                ('contenido_mensaje', models.TextField()),
                ('usuario', models.ForeignKey(related_name='historial_usuario', to='han_app.Usuario')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='grupo',
            name='integrantes',
            field=models.ManyToManyField(related_name='usuario_grupo', to='han_app.Usuario'),
        ),
    ]
