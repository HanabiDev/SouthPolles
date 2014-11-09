#encoding: utf-8

from django.db import models
from redactor.fields import RedactorField
from django.core.validators import MinValueValidator, MaxValueValidator

from django.core.exceptions import ValidationError
from datetime import date
from django.template.defaultfilters import date as _date

def validate_birthday(birth_date):
	min_date = date(1940, 1, 1)
	max_date = date(1998, 12, 31)
	if birth_date < min_date or birth_date > max_date:
		format_min_date = _date(min_date, "d \d\e b \d\e Y")
		format_max_date = _date(max_date, "d \d\e b \d\e Y")
		raise ValidationError(u'Sólo fechas entre %s y %s' % (format_min_date, format_max_date))


# Create your models here.
class Municipio(models.Model):
    nombre = models.CharField(max_length=40)

    def __unicode__(self):
    	return self.nombre

class Carreer(models.Model):
	BASES = (
		('T', 'Tunja'),
		('D', 'Duitama'),
		('S', 'Sogamoso'),
		('C', 'Chiquinquirá')
	)

	nombre = models.CharField(max_length=200)
	base = models.CharField(verbose_name=u'Sede', max_length=1, choices=BASES)

	def __unicode__(self):
		BASES = (
			('T', 'Tunja'),
			('D', 'Duitama'),
			('S', 'Sogamoso'),
			('C', 'Chiquinquirá')
		)
		return self.nombre + " - " + self.get_base_display()

class Person(models.Model):
	CHILDREN = ((0, 'Cero'), (1, 'Uno'), (2, 'Dos'), (3, 'Tres'), (4, 'Más de tres'), )

	GENRES = (
		('M', 'Masculino'),
		('F', 'Femenino')
	)
	
	STRATUMS = (
		(1, 'Uno (1)'),
		(2, 'Dos (2)'),
		(3, 'Tres (3)'),
		(4, 'Cuatro (4)'),
		(5, 'Cinco (5)'),
		(6, 'Seis (6)')
	)

	STATUS = (
		('S','Soltero'),
		('C','Casado'),
		('D','Divorciado'),
		('V','Viudo'),
		('U','Unión Libre')
	)

	ROLES = (
		('A', 'Alumno'),
		('D', 'Docente'),
		('F', 'Funcionario')
	)

	BASES = (
		('T', 'Tunja'),
		('D', 'Duitama'),
		('S', 'Sogamoso'),
		('C', 'Chiquinquirá')
	)
	
	name = models.CharField(verbose_name=u'Nombre (Opcional)', max_length=300, null=True, blank=True)
	lastname = models.CharField(verbose_name=u'Apellidos (Opcional)', max_length=300, null=True, blank=True)
	genre = models.CharField(verbose_name=u'Género', max_length=1, choices=GENRES)
	birth_date = models.DateField(verbose_name=u'Fecha de nacimiento', validators=[validate_birthday])
	origin_city = models.ForeignKey(Municipio, verbose_name=u'Ciudad de Origen')
	actual_city = models.ForeignKey(Municipio,verbose_name=u'Ciudad de Residencia', related_name='residencia')
	status = models.CharField(verbose_name=u'Estado civil (Opcional)', max_length=1, choices=STATUS, null=True, blank=True)
	children = models.CharField(verbose_name=u'Hijos (Opcional)', max_length=1, choices=CHILDREN, null=True, blank=True)
	religion = models.CharField(verbose_name=u'Credo religioso (Opcional)', max_length=100, null=True, blank=True)
	stratum = models.IntegerField(verbose_name=u'Estrato', max_length=1, choices=STRATUMS)
	role = models.CharField(verbose_name=u'Cargo (Opcional)', max_length=1, choices=ROLES, null=True, blank=True)
	career = models.ForeignKey(Carreer, verbose_name=u'Programa')
	semester = models.IntegerField(verbose_name=u'Semestre', validators=[MinValueValidator(1), MaxValueValidator(12)])
	code = models.CharField(verbose_name=u'Código (Opcional)', max_length=20, null=True, blank=True)
	base = models.CharField(verbose_name=u'Sede', max_length=1, choices=BASES)

	class Meta:
		verbose_name = u'Persona'
		verbose_name_plural = u'Personas'



class Poll(models.Model):
	title = models.CharField(verbose_name=u'Título', max_length=255, unique=True)
	#author = models.
	start_date = models.DateTimeField(verbose_name=u'Fecha de Inicio')
	end_date = models.DateTimeField(verbose_name=u'Fecha de Finalización')
	description = RedactorField(verbose_name=u'Descripción', blank=True)
	instructions = RedactorField(verbose_name=u'Instrucciones', blank=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u'Prueba'

class PollSection(models.Model):
	poll = models.ForeignKey(Poll, verbose_name=u'Prueba')
	text = models.CharField(verbose_name=u'Título', max_length=500)
	index = models.IntegerField(verbose_name=u'Orden')

	def __unicode__(self):
		return self.text

	class Meta:
		verbose_name = 'Sección'
		verbose_name_plural = "Secciones"
		ordering = ['index']

class Question(models.Model):
	poll = models.ForeignKey(Poll, verbose_name=u'Prueba')
	section = models.ForeignKey(PollSection, verbose_name=u'Sección')
	text = models.TextField(verbose_name=u'Texto de la pregunta')
	index = models.IntegerField(verbose_name=u'Orden')
	instructions = models.TextField(verbose_name=u'Instrucciones (Opcional)', null=True, blank=True)

	def __unicode__(self):
		return str(self.index) + '. ' + self.text

	class Meta:
		verbose_name = u'Pregunta'
		ordering = ['index']



class Option(models.Model):
	question = models.ForeignKey(Question, verbose_name=u'Pregunta')
	text = models.CharField(verbose_name=u'Texto de la opción', max_length=500)
	index = models.IntegerField(verbose_name=u'Orden')

	def __unicode__(self):
		return 'Pregunta ' + str(self.question.index) + ' > ' + self.text
	
	class Meta:
		verbose_name = u'Opción'
		verbose_name_plural = u'Opciones'
		ordering = ['question','index']

