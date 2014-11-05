# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20141101_0202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='person',
            name='actual_city',
            field=models.ForeignKey(related_name='residencia', verbose_name='Ciudad de Residencia', to='polls.Municipio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='origin_city',
            field=models.ForeignKey(verbose_name='Ciudad de Origen', to='polls.Municipio'),
            preserve_default=True,
        ),
    ]
