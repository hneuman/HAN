# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0011_auto_20171003_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buzon_pendientes',
            name='asignado_hora',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 3, 21, 42, 27, 138564)),
        ),
    ]
