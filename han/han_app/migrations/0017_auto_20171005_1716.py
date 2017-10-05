# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0016_auto_20171005_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario_historial_mensaje',
            name='usuario2',
            field=models.ForeignKey(related_name='historial_usuario_detalle', default=False, to='han_app.Usuario'),
        ),
    ]
