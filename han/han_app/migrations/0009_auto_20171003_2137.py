# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0008_auto_20160811_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buzon_pendientes',
            name='asignado_hora',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 3, 21, 37, 56, 438744)),
        ),
    ]
