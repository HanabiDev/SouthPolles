# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20141104_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carreer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('base', models.CharField(max_length=1, verbose_name='Sede', choices=[(b'T', b'Tunja'), (b'D', b'Duitama'), (b'S', b'Sogamoso'), (b'C', b'Chiquinquir\xc3\xa1')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='person',
            name='career',
            field=models.ForeignKey(verbose_name='Programa', to='polls.Carreer'),
            preserve_default=True,
        ),
    ]
