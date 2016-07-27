# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0004_auto_20151215_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_grupo', models.CharField(max_length=100)),
                ('integrantes', models.ManyToManyField(to='han_app.Usuario')),
            ],
        ),
    ]
