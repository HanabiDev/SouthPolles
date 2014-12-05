#encoding: utf-8
from django.db import models
from redactor.fields import RedactorField
from polls.models import Question, Poll

class Report(models.Model):
	title = models.CharField(max_length=500, verbose_name=u'Título del Informe')
	poll = models.ForeignKey(Poll, verbose_name=u'Prueba')
	report_date = models.DateField(auto_now=True, verbose_name=u'Fecha')
	expert = models.CharField(max_length=200, verbose_name=u'Autor')
	description = RedactorField(verbose_name=u'Descripción')

	def __unicode__(self):
		return self.title

class ReportSection(models.Model):

	VARIABLES = (
		('genre','Género'),('birth_date','Edad'),
		('origin_dept','Departamento de Origen'),('actual_dept','Departamento de Residencia'),
		('origin_city','Ciudad de Origen'),('actual_city','Ciudad de Residencia'),
		('status','Estado civil'),('children','Hijos'),
		('stratum','Estrato'),('role','Cargo'),
		('career','Programa'),('semester','Semestre'),
		('base','Sede')
	)

	report = models.ForeignKey(Report, verbose_name=u'Reporte')
	title = models.CharField(max_length=500, verbose_name=u'Título de la sección')
	attribute = models.CharField(max_length=50, verbose_name=u'Variable', choices=VARIABLES)
	diagnostic = RedactorField(verbose_name=u'Diagnóstico')
	questions = models.ManyToManyField(Question, verbose_name=u'Preguntas')

	class Meta:
		unique_together =  ("report", "attribute")