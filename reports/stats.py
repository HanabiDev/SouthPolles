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


def get_stats_by_birth(questions, id_ranges):
	question_stats = []

	clean_ids = []
	for ids in id_ranges:
		ids = [id[0] for id in ids]
		clean_ids.append(ids)
		
	range1_answers = Answer.objects.filter(application__person__id__in=clean_ids[0])
	range2_answers = Answer.objects.filter(application__person__id__in=clean_ids[1])
	range3_answers = Answer.objects.filter(application__person__id__in=clean_ids[2])
	range4_answers = Answer.objects.filter(application__person__id__in=clean_ids[3])

	for question in questions:
		series = [serie[0] for serie in question.option_set.all().values_list('text').order_by('index')]

		range1_count = range1_answers.filter(
			option__question=question
		).order_by('index').values_list('option__text').order_by().annotate(Count('option__text'))

		range2_count = range2_answers.filter(
			option__question=question
		).order_by('index').values_list('option__text').order_by().annotate(Count('option__text'))

		range3_count = range3_answers.filter(
			option__question=question
		).order_by('index').values_list('option__text').order_by().annotate(Count('option__text'))
		
		range4_count = range4_answers.filter(
			option__question=question
		).order_by('index').values_list('option__text').order_by().annotate(Count('option__text'))

		range1_count = dict(range1_count)
		range2_count = dict(range2_count)
		range3_count = dict(range3_count)
		range4_count = dict(range4_count)

		for label in series:
			if not range1_count.get(label):
				range1_count[label]=0

		for label in series:
			if not range2_count.get(label):
				range2_count[label]=0

		for label in series:
			if not range3_count.get(label):
				range3_count[label]=0

		for label in series:
			if not range4_count.get(label):
				range4_count[label]=0

		range1_count = collections.OrderedDict(sorted(range1_count.items()))
		range2_count = collections.OrderedDict(sorted(range2_count.items()))
		range3_count = collections.OrderedDict(sorted(range3_count.items()))
		range4_count = collections.OrderedDict(sorted(range4_count.items()))
		
		range1_values = []
		range2_values = []
		range3_values = []
		range4_values = []

		for key,value in range1_count.iteritems():
			range1_values.append(value)

		for key,value in range2_count.iteritems():
			range2_values.append(value)

		for key,value in range3_count.iteritems():
			range3_values.append(value)

		for key,value in range4_count.iteritems():
			range4_values.append(value)

		s1 = [range1_values[0],range2_values[0],range3_values[0],range4_values[0]]
		s2 = [range1_values[1],range2_values[1],range3_values[1],range4_values[1]]
		s3 = [range1_values[2],range2_values[2],range3_values[2],range4_values[2]]

		question_stats.append({
			'question_id':question.id,
			'question': str(question.index)+": "+question.text,
			'series':series, 'ticks':['Entre 15 y 20', 'Entre 20 y 25', 'Entre 25 y 30', 'Más de 30'], 'data':[s1, s2, s3]
		})
	return question_stats

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





