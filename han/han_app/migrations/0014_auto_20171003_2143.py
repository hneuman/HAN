# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0013_auto_20171003_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buzon_pendientes',
            name='asignado_hora',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
