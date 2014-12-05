# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='T\xedtulo del Informe')),
                ('report_date', models.DateField(auto_now=True, verbose_name='Fecha')),
                ('expert', models.CharField(max_length=200, verbose_name='Autor')),
                ('description', redactor.fields.RedactorField(verbose_name='Descripci\xf3n')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReportSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='T\xedtulo de la secci\xf3n')),
                ('attribute', models.CharField(max_length=50, verbose_name='Variable', choices=[(b'genre', b'G\xc3\xa9nero'), (b'birth_date', b'Edad'), (b'origin_dept', b'Departamento de Origen'), (b'actual_dept', b'Departamento de Residencia'), (b'origin_city', b'Ciudad de Origen'), (b'actual_city', b'Ciudad de Residencia'), (b'status', b'Estado civil'), (b'children', b'Hijos'), (b'stratum', b'Estrato'), (b'role', b'Cargo'), (b'career', b'Programa'), (b'semester', b'Semestre'), (b'base', b'Sede')])),
                ('diagnostic', redactor.fields.RedactorField(verbose_name='Diagn\xf3stico')),
                ('questiones', models.ManyToManyField(to='polls.Question', verbose_name='Preguntas')),
                ('report', models.ForeignKey(verbose_name='Reporte', to='reports.Report')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='reportsection',
            unique_together=set([('report', 'attribute')]),
        ),
    ]
