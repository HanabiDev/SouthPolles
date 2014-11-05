# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=500, verbose_name='Texto de la opci\xf3n')),
                ('index', models.IntegerField(verbose_name='Orden')),
            ],
            options={
                'ordering': ['index'],
                'verbose_name': 'Opci\xf3n',
                'verbose_name_plural': 'Opciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.CharField(max_length=1, verbose_name='G\xe9nero', choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('age', models.IntegerField(verbose_name='Edad')),
                ('stratum', models.IntegerField(max_length=1, verbose_name='Estrato', choices=[(1, b'Uno (1)'), (2, b'Dos (2)'), (3, b'Tres (3)'), (4, b'Cuatro (4)'), (5, b'Cinco (5)'), (6, b'Seis (6)')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=500, verbose_name='T\xedtulo')),
                ('start_date', models.DateTimeField(verbose_name='Fecha de Inicio')),
                ('end_date', models.DateTimeField(verbose_name='Fecha de Finalizaci\xf3n')),
                ('description', redactor.fields.RedactorField(verbose_name='Descripci\xf3n', blank=True)),
                ('instructions', redactor.fields.RedactorField(verbose_name='Instrucciones', blank=True)),
            ],
            options={
                'verbose_name': 'Prueba',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PollSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=500, verbose_name='T\xedtulo')),
                ('index', models.IntegerField(verbose_name='Orden')),
                ('poll', models.ForeignKey(verbose_name='Prueba', to='polls.Poll')),
            ],
            options={
                'ordering': ['index'],
                'verbose_name': 'Secci\xf3n',
                'verbose_name_plural': 'Secciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='Texto de la pregunta')),
                ('index', models.IntegerField(verbose_name='Orden')),
                ('instructions', models.TextField(null=True, verbose_name='Instrucciones (Opcional)', blank=True)),
                ('poll', models.ForeignKey(verbose_name='Prueba', to='polls.Poll')),
                ('section', models.ForeignKey(verbose_name='Secci\xf3n', to='polls.PollSection')),
            ],
            options={
                'ordering': ['index'],
                'verbose_name': 'Pregunta',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(verbose_name='Pregunta', to='polls.Question'),
            preserve_default=True,
        ),
    ]
