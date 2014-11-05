# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20141031_0613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
        migrations.AddField(
            model_name='person',
            name='actual_city',
            field=models.CharField(default=datetime.datetime(2014, 11, 1, 0, 28, 51, 826320, tzinfo=utc), max_length=200, verbose_name='Ciudad de Residencia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='base',
            field=models.CharField(default='Tunja', max_length=4, verbose_name='Sede'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2014, 11, 1, 0, 29, 33, 99838, tzinfo=utc), verbose_name='Fecha de nacimiento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='career',
            field=models.CharField(default='', max_length=2, verbose_name='Programa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='children',
            field=models.CharField(default='N', max_length=1, verbose_name='Hijos (Opcional)', choices=[(b'S', b'Si'), (b'N', b'No')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='code',
            field=models.CharField(max_length=20, null=True, verbose_name='C\xf3digo (Opcional)', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='lastname',
            field=models.CharField(max_length=300, null=True, verbose_name='Apellidos (Opcional)', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=300, null=True, verbose_name='Nombre (Opcional)', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='origin_city',
            field=models.CharField(default='Tunja', max_length=200, verbose_name='Ciudad de Origen'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='religion',
            field=models.CharField(max_length=100, null=True, verbose_name='Credo religioso (Opcional)', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Cargo (Opcional)', choices=[(b'A', b'Alumno'), (b'D', b'Docente'), (b'F', b'Funcionario')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='semester',
            field=models.IntegerField(default=1, verbose_name='Semestre', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Estado civil (Opcional)', choices=[(b'S', b'Soltero'), (b'C', b'Casado'), (b'D', b'Divorciado'), (b'V', b'Viudo')]),
            preserve_default=True,
        ),
    ]
