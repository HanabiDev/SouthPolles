#encoding: utf-8

from frontend.models import Answer
from polls.models import Carreer
from django.db.models import Count
import json

import collections

def get_stats_by_genre(questions):

	question_stats = []

	male_answers = Answer.objects.filter(application__person__genre='M')
	female_answers = Answer.objects.filter(application__person__genre='F')

	for question in questions:
		series = [serie[0] for serie in question.option_set.all().values_list('text').order_by('index')]

		male_count = male_answers.filter(
			option__question=question
		).order_by('index').values_list('option__text').order_by().annotate(Count('option__text'))

		female_count = female_answers.filter(
			option__question=question
		).order_by('index').values_list('option__text').order_by().annotate(Count('option__text'))
		
		male_count = dict(male_count)
		female_count = dict(female_count)

		for label in series:
			if not male_count.get(label):
				male_count[label]=0

		for label in series:
			if not female_count.get(label):
				female_count[label]=0

		male_count = collections.OrderedDict(sorted(male_count.items()))
		female_count = collections.OrderedDict(sorted(female_count.items()))
		
		male_values = []
		female_values = []

		for key,value in male_count.iteritems():
			male_values.append(value)

		for key,value in female_count.iteritems():
			female_values.append(value)

		s1 = [male_values[0],female_values[0]]
		s2 = [male_values[1],female_values[1]]
		s3 = [male_values[2],female_values[2]]

		question_stats.append({
			'question_id':question.id,
			'question': str(question.index)+": "+question.text,
			'series':series, 'ticks':['Hombre', 'Mujer'], 'data':[s1, s2, s3]
		})

	return question_stats


def get_stats_by_birth(questions):
	pass

def get_stats_by_status(questions):

	question_stats = []

	status_answers = []
	
	for status in ['S', 'C', 'D', 'V', 'U']:
		status_answers.append(Answer.objects.filter(application__person__status=status))


	for question in questions:
		series = [serie[0] for serie in question.option_set.all().values_list('text').order_by('index')]

		s1 = []
		s2 = []
		s3 = []

		for index, answers in enumerate(status_answers):
			status_count = answers.filter(
				option__question=question
			).order_by('index').values_list('option__text').order_by().annotate(Count('option__text'))

		
			status_count = dict(status_count)

			for label in series:
				if not status_count.get(label):
					status_count[label]=0

			status_count = collections.OrderedDict(sorted(status_count.items()))
			status_values = []

			for key,value in status_count.iteritems():
				status_values.append(value)

			value1, value2, value3 = status_values
			s1.append(value1)
			s2.append(value2)
			s3.append(value3)			

		question_stats.append({
			'question_id':question.id,
			'question': str(question.index)+": "+question.text,
			'series':series, 
			'ticks':['Soltero', 'Casado', 'Divorciado', 'Viudo', 'Unión Libre'], 
			'data':[s1, s2, s3]
		})

	return question_stats

def get_stats_by_children(questions):
	question_stats = []

	stratum_answers = []
	
	for children in range(0,5):
		stratum_answers.append(Answer.objects.filter(application__person__children=children))


	for question in questions:
		series = [serie[0] for serie in question.option_set.all().values_list('text').order_by('index')]

		s1 = []
		s2 = []
		s3 = []

		for index, answers in enumerate(stratum_answers):
			stratum_count = answers.filter(
				option__question=question
			).order_by('index').values_list('option__text').order_by().annotate(Count('option__text'))

		
			stratum_count = dict(stratum_count)

			for label in series:
				if not stratum_count.get(label):
					stratum_count[label]=0

			stratum_count = collections.OrderedDict(sorted(stratum_count.items()))
			stratum_values = []

			for key,value in stratum_count.iteritems():
				stratum_values.append(value)

			value1, value2, value3 = stratum_values
			s1.append(value1)
			s2.append(value2)
			s3.append(value3)			

		question_stats.append({
			'question_id':question.id,
			'question': str(question.index)+": "+question.text,
			'series':series, 
			'ticks':['Cero', 'Uno', 'Dos', 'Tres', 'Más de tres'], 
			'data':[s1, s2, s3]
		})

	return question_stats	

def get_stats_by_stratum(questions):

	question_stats = []

	stratum_answers = []
	
	for stratum in range(1,7):
		stratum_answers.append(Answer.objects.filter(application__person__stratum=stratum))


	for question in questions:
		series = [serie[0] for serie in question.option_set.all().values_list('text').order_by('index')]

		s1 = []
		s2 = []
		s3 = []

		for index, answers in enumerate(stratum_answers):
			stratum_count = answers.filter(
				option__question=question
			).order_by('index').values_list('option__text').order_by().annotate(Count('option__text'))

		
			stratum_count = dict(stratum_count)

			for label in series:
				if not stratum_count.get(label):
					stratum_count[label]=0

			stratum_count = collections.OrderedDict(sorted(stratum_count.items()))
			stratum_values = []

			for key,value in stratum_count.iteritems():
				stratum_values.append(value)

			value1, value2, value3 = stratum_values
			s1.append(value1)
			s2.append(value2)
			s3.append(value3)			

		question_stats.append({
			'question_id':question.id,
			'question': str(question.index)+": "+question.text,
			'series':series, 
			'ticks':range(1,7), 
			'data':[s1, s2, s3]
		})

	return question_stats

def get_stats_by_role(questions):
	question_stats = []

	role_answers = []
	
	for role in ['A', 'D', 'F']:
		role_answers.append(Answer.objects.filter(application__person__role=role))


	for question in questions:
		series = [serie[0] for serie in question.option_set.all().values_list('text').order_by('index')]

		s1 = []
		s2 = []
		s3 = []

		for index, answers in enumerate(role_answers):
			role_count = answers.filter(
				option__question=question
			).order_by('index').values_list('option__text').order_by().annotate(Count('option__text'))

		
			role_count = dict(role_count)

			for label in series:
				if not role_count.get(label):
					role_count[label]=0

			role_count = collections.OrderedDict(sorted(role_count.items()))
			role_values = []

			for key,value in role_count.iteritems():
				role_values.append(value)

			value1, value2, value3 = role_values
			s1.append(value1)
			s2.append(value2)
			s3.append(value3)
			
		question_stats.append({
			'question_id':question.id,
			'question': str(question.index)+": "+question.text,
			'series':series, 'ticks':['Alumno', 'Docente', 'Funcionario'], 'data':[s1, s2, s3]
		})

	return question_stats	

def get_stats_by_carreer(questions, carreers):
	question_stats = []

	carreer_answers = []
	carreer_labels = []

	for carreer in carreers:
		label = Carreer.objects.filter(id=carreer).values_list('nombre')
		carreer_labels.append(label[0])
		carreer_answers.append(Answer.objects.filter(application__person__career=carreer))

	for question in questions:
		series = [serie[0] for serie in question.option_set.all().values_list('text').order_by('index')]

		s1 = []
		s2 = []
		s3 = []

		for index, answers in enumerate(carreer_answers):
			carreer_count = answers.filter(
				option__question=question
			).order_by('index').values_list('option__text').order_by().annotate(Count('option__text'))

		
			carreer_count = dict(carreer_count)

			for label in series:
				if not carreer_count.get(label):
					carreer_count[label]=0

			carreer_count = collections.OrderedDict(sorted(carreer_count.items()))
			carreer_values = []

			for key,value in carreer_count.iteritems():
				carreer_values.append(value)

			value1, value2, value3 = carreer_values
			s1.append(value1)
			s2.append(value2)
			s3.append(value3)

		print carreer_labels

		question_stats.append({
			'question_id':question.id,
			'question': str(question.index)+": "+question.text,
			'series':series, 'ticks':carreer_labels, 'data':[s1, s2, s3]
		})

	return question_stats

def get_stats_by_semester(questions):
	question_stats = []

	semester_answers = []
	
	for semester in range(1,13):
		semester_answers.append(Answer.objects.filter(application__person__semester=semester))


	for question in questions:
		series = [serie[0] for serie in question.option_set.all().values_list('text').order_by('index')]

		s1 = []
		s2 = []
		s3 = []

		for index, answers in enumerate(semester_answers):
			semester_count = answers.filter(
				option__question=question
			).order_by('index').values_list('option__text').order_by().annotate(Count('option__text'))

		
			semester_count = dict(semester_count)

			for label in series:
				if not semester_count.get(label):
					semester_count[label]=0

			semester_count = collections.OrderedDict(sorted(semester_count.items()))
			semester_values = []

			for key,value in semester_count.iteritems():
				semester_values.append(value)

			value1, value2, value3 = semester_values
			s1.append(value1)
			s2.append(value2)
			s3.append(value3)

		question_stats.append({
			'question_id':question.id,
			'question': str(question.index)+": "+question.text,
			'series':series, 'ticks':range(1,13), 'data':[s1, s2, s3]
		})

	return question_stats

def get_stats_by_base(questions):
	question_stats = []

	base_answers = []
	
	for base in ['T', 'D', 'S', 'C']:
		base_answers.append(Answer.objects.filter(application__person__base=base))


	for question in questions:
		series = [serie[0] for serie in question.option_set.all().values_list('text').order_by('index')]

		s1 = []
		s2 = []
		s3 = []

		for index, answers in enumerate(base_answers):
			base_count = answers.filter(
				option__question=question
			).order_by('index').values_list('option__text').order_by().annotate(Count('option__text'))

		
			base_count = dict(base_count)

			for label in series:
				if not base_count.get(label):
					base_count[label]=0

			base_count = collections.OrderedDict(sorted(base_count.items()))
			base_values = []

			for key,value in base_count.iteritems():
				base_values.append(value)

			value1, value2, value3 = base_values
			s1.append(value1)
			s2.append(value2)
			s3.append(value3)

		question_stats.append({
			'question_id':question.id,
			'question': str(question.index)+": "+question.text,
			'series':series, 'ticks':['Tunja', 'Duitama', 'Sogamoso', 'Chiquinquirá'], 'data':[s1, s2, s3]
		})

	return question_stats





