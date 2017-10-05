# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0019_auto_20171005_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='codigo_u',
            field=models.CharField(default=b'no Codigo', max_length=100),
        ),
    ]
