# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('han_app', '0005_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario_envia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_usuario_envia', models.CharField(max_length=100)),
                ('id_usuario_envia', models.CharField(max_length=100)),
                ('contador', models.IntegerField()),
            ],
        ),
    ]
