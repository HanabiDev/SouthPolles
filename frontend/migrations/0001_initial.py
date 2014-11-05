# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20141031_0613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField()),
                ('person', models.ForeignKey(to='polls.Person')),
                ('poll', models.ForeignKey(to='polls.Poll')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='answer',
            name='application',
            field=models.ForeignKey(to='frontend.Application'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='option',
            field=models.ForeignKey(to='polls.Option'),
            preserve_default=True,
        ),
    ]
