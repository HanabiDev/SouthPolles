# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportsection',
            name='questions',
            field=models.ManyToManyField(to='polls.Question', verbose_name='Preguntas'),
            preserve_default=True,
        ),
    ]
