# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0007_buzon_enviados_usuario_envia'),
    ]

    operations = [
        migrations.AddField(
            model_name='buzon_pendientes',
            name='asignado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='buzon_pendientes',
            name='asignado_a',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='buzon_pendientes',
            name='asignado_hora',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 11, 19, 20, 26, 413212)),
        ),
    ]
