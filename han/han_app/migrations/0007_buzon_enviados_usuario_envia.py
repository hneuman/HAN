# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0006_usuario_envia'),
    ]

    operations = [
        migrations.AddField(
            model_name='buzon_enviados',
            name='usuario_envia',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
