# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0015_auto_20171004_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario_historial_mensaje',
            name='usuario2',
            field=models.ForeignKey(related_name='historial_usuario_detalle', default=1, to='han_app.Usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario_historial_mensaje',
            name='usuario',
            field=models.ForeignKey(related_name='historial_usuario', to='han_app.Usuario'),
        ),
    ]
