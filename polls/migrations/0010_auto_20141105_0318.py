# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20141105_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='code',
            field=models.CharField(max_length=20, unique=True, null=True, verbose_name='C\xf3digo (Opcional)', blank=True),
            preserve_default=True,
        ),
    ]
