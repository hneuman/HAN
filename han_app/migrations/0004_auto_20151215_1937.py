# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0003_buzon_entrada_buzon_enviados_buzon_pendientes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buzon_entrada',
            name='contenido_mensaje',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='buzon_enviados',
            name='contenido_mensaje',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='buzon_pendientes',
            name='contenido_mensaje',
            field=models.TextField(),
        ),
    ]
