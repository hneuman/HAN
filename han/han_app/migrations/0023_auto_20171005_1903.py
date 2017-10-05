# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0022_auto_20171005_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='integrantes',
            field=models.ManyToManyField(related_name='usuario_grupo', to='han_app.Usuario'),
        ),
    ]
