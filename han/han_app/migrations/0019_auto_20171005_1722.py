# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0018_remove_usuario_historial_mensaje_usuario2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario_historial_mensaje',
            options={'ordering': ('id',)},
        ),
    ]
