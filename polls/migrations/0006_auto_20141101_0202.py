# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20141101_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='base',
            field=models.CharField(max_length=1, verbose_name='Sede', choices=[(b'T', b'Tunja'), (b'D', b'Duitama'), (b'S', b'Sogamoso'), (b'C', b'Chiquinquir\xc3\xa1')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='children',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Hijos (Opcional)', choices=[(b'S', b'Si'), (b'N', b'No')]),
            preserve_default=True,
        ),
    ]
