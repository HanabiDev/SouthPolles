# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20141031_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(verbose_name='Edad', validators=[django.core.validators.MinValueValidator(14), django.core.validators.MaxValueValidator(28)]),
            preserve_default=True,
        ),
    ]
