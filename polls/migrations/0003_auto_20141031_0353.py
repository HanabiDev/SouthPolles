# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20141031_0348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='option',
            options={'ordering': ['question', 'index'], 'verbose_name': 'Opci\xf3n', 'verbose_name_plural': 'Opciones'},
        ),
        migrations.AlterOrderWithRespectTo(
            name='option',
            order_with_respect_to=None,
        ),
    ]
