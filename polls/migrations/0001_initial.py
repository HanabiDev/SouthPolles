# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import polls.models
import redactor.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
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
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
                ('departamento', models.ForeignKey(to='polls.Departamento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=500, verbose_name='Texto de la opci\xf3n')),
                ('index', models.IntegerField(verbose_name='Orden')),
            ],
            options={
                'ordering': ['question', 'index'],
                'verbose_name': 'Opci\xf3n',
                'verbose_name_plural': 'Opciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, null=True, verbose_name='Nombre (Opcional)', blank=True)),
                ('lastname', models.CharField(max_length=300, null=True, verbose_name='Apellidos (Opcional)', blank=True)),
                ('genre', models.CharField(max_length=1, verbose_name='G\xe9nero', choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('birth_date', models.DateField(verbose_name='Fecha de nacimiento', validators=[polls.models.validate_birthday])),
                ('status', models.CharField(blank=True, max_length=1, null=True, verbose_name='Estado civil (Opcional)', choices=[(b'S', b'Soltero'), (b'C', b'Casado'), (b'D', b'Divorciado'), (b'V', b'Viudo'), (b'U', b'Uni\xc3\xb3n Libre')])),
                ('children', models.CharField(blank=True, max_length=1, null=True, verbose_name='Hijos (Opcional)', choices=[(b'0', b'Cero'), (b'1', b'Uno'), (b'2', b'Dos'), (b'3', b'Tres'), (b'4', b'M\xc3\xa1s de tres')])),
                ('religion', models.CharField(max_length=100, null=True, verbose_name='Credo religioso (Opcional)', blank=True)),
                ('stratum', models.IntegerField(max_length=1, verbose_name='Estrato', choices=[(1, b'Uno (1)'), (2, b'Dos (2)'), (3, b'Tres (3)'), (4, b'Cuatro (4)'), (5, b'Cinco (5)'), (6, b'Seis (6)')])),
                ('role', models.CharField(blank=True, max_length=1, null=True, verbose_name='Cargo (Opcional)', choices=[(b'A', b'Alumno'), (b'D', b'Docente'), (b'F', b'Funcionario')])),
                ('semester', models.IntegerField(verbose_name='Semestre', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('code', models.CharField(max_length=20, null=True, verbose_name='C\xf3digo (Opcional)', blank=True)),
                ('base', models.CharField(max_length=1, verbose_name='Sede', choices=[(b'T', b'Tunja'), (b'D', b'Duitama'), (b'S', b'Sogamoso'), (b'C', b'Chiquinquir\xc3\xa1')])),
                ('actual_city', models.ForeignKey(related_name='residencia', verbose_name='Ciudad de Residencia', to='polls.Municipio')),
                ('actual_dept', models.ForeignKey(related_name='depto_residencia', verbose_name=b'Departamento de Residencia', to='polls.Departamento')),
                ('career', models.ForeignKey(verbose_name='Programa', to='polls.Carreer')),
                ('origin_city', models.ForeignKey(verbose_name='Ciudad de Origen', to='polls.Municipio')),
                ('origin_dept', models.ForeignKey(verbose_name=b'Departamento de Origen', to='polls.Departamento')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255, verbose_name='T\xedtulo')),
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
