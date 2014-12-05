# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
        ('reports', '0002_auto_20141117_0542'),
    ]

    operations = [  
        migrations.AddField(
            model_name='report',
            name='poll',
            field=models.ForeignKey(default=1, verbose_name='Prueba', to='polls.Poll'),
            preserve_default=False,
        ),
    ]
