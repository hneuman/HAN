# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0014_auto_20171003_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario_historial_mensaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_mensaje', models.CharField(max_length=100)),
                ('numero_telefono', models.CharField(max_length=100)),
                ('contenido_mensaje', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='codigo_u',
            field=models.CharField(default=b'no Codigo', max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='usuario_historial_mensaje',
            name='usuario',
            field=models.ForeignKey(to='han_app.Usuario'),
        ),
    ]
