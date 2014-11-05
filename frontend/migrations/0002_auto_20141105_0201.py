# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20141105_0201'),
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=0, to='polls.Question'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
