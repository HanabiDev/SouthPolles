# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportsection',
            old_name='sec_questions',
            new_name='questions',
        ),
    ]
