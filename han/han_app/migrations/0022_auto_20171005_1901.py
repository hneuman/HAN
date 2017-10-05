# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0021_auto_20171005_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='codigo_u',
            field=models.CharField(default=b'no Codigo', max_length=100, serialize=False, primary_key=True),
        ),
    ]
