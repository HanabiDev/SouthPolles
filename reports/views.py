#encoding: utf-8

from django.shortcuts import redirect, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext

from models import Report, ReportSection
from forms import ReportForm, ReportSectionForm

from polls.models import Person, Question
from stats import *

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required


def admin_login(request):

	if request.user.is_authenticated():
		print request.user

		return redirect(reverse('report_home'))

	if request.method == 'GET':
		form = AuthenticationForm(request)

		return render_to_response(
			'login.html',
			{'form':form},
      		context_instance=RequestContext(request)
	    )

	elif request.method == 'POST':

		form = AuthenticationForm(request.POST)

		username = request.POST.get('username')
		password = request.POST.get('password')

		form.fields['username'].initial = username

		if not username:
			form_err = {'username_errors':'Ingresa un nombre de usuario'}
			return render_to_response(
				'login.html',
				{'form':form, 'form_err':form_err},
				context_instance=RequestContext(request)
			)
		if not password:
			form_err = {'password_errors':'Ingresa una contraseña'}
			return render_to_response(
				'login.html',
				{'form':form, 'form_err':form_err},
				context_instance=RequestContext(request)
			)

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect(reverse('report_home'))
			else:
				form_err = {}
				form_err['error'] = 'Esta cuenta está deshabilitada'

				return render_to_response(
					'login.html',
					{'form':form, 'form_err':form_err},
					context_instance=RequestContext(request)
				)
		else:
			form_err = {}
			form_err['error'] = 'Esta cuenta no existe o la contraseña no coincide'
			return render_to_response(
				'login.html',
				{'form':form, 'form_err':form_err},
				context_instance=RequestContext(request)
			)

def admin_logout(request):
	if not request.user.is_authenticated():
		return redirect('login')

	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
	reports = Report.objects.all()
	return render_to_response('reports_index.html', {'reports': reports})

@login_required(login_url='login')
def create_report(request):
	if request.method == 'GET':
		form = ReportForm()
		return render_to_response('add_edit_report.html', {'form': form}, context_instance=RequestContext(request))

	if request.method == 'POST':
		form = ReportForm(request.POST)
		if form.is_valid():
			new_report = form.save()
			return redirect(reverse('edit_report', args=(new_report.id,)))

		return render_to_response('add_edit_report.html', {'form': form}, context_instance=RequestContext(request))

@login_required(login_url='login')
def edit_report(request, report_id):

	report = Report.objects.get(id=report_id)
	
	if request.method == 'GET':
		form = ReportForm(instance=report)

		return render_to_response('add_edit_report.html', 
			{'form':form, 'editing':True, 'report':report}, 
			context_instance=RequestContext(request)
		)

	if request.method == 'POST':
		form = ReportForm(request.POST, instance=report)
		if form.is_valid():
			report = form.save()
			return redirect(reverse('report_home'))

		return render_to_response('add_edit_report.html', 
			{'form':form, 'editing':True, 'report':report}, 
			context_instance=RequestContext(request)
		)

@login_required(login_url='login')
def delete_report(request, report_id):
	report = Report.objects.get(id=report_id)
	report.delete()

	return redirect(reverse('report_home'))

@login_required(login_url='login')
def add_section(request, report_id):
	
	if request.method == 'GET':
		form = ReportSectionForm()
		return render_to_response('add_edit_section.html', {'form': form, 'report_id':report_id}, context_instance=RequestContext(request))

	if request.method == 'POST':
		form = ReportSectionForm(request.POST)
		if form.is_valid():
			new_section = form.save()
			return redirect(reverse('edit_report', args=(report_id,)))

		return render_to_response('add_edit_section.html', {'form': form, 'report_id':report_id}, context_instance=RequestContext(request))

@login_required(login_url='login')
def edit_section(request, report_id, section_id):
	
	section = ReportSection.objects.get(id=section_id)

	if request.method == 'GET':
		form = ReportSectionForm(instance=section)
		return render_to_response('add_edit_section.html', 
			{'form': form, 'editing':True,'report_id':report_id, 'section_id':section_id}, 
			context_instance=RequestContext(request)
		)

	if request.method == 'POST':
		form = ReportSectionForm(request.POST, instance=section)
		if form.is_valid():
			section = form.save()
			return redirect(reverse('edit_report', args=(report_id,)))

		return render_to_response('add_edit_section.html', 
			{'form': form, 'editing':True,'report_id':report_id, 'section_id':section_id}, 
			context_instance=RequestContext(request)
		)

@login_required(login_url='login')
def delete_section(request, report_id, section_id):

	section = ReportSection.objects.get(id=section_id)
	section.delete()
	return redirect(reverse('edit_report', args=(report_id,)))

@login_required(login_url='login')
def report_observ(request, report_id):

	report = Report.objects.get(id=report_id)

	section_reports = []
	for section in report.reportsection_set.all():
		section_reports.append({
			'section': section,
			'section_report': get_section_report(section)
		})


	return render_to_response(
		'report.html', 
		{'report':report,'section_reports':section_reports},
		context_instance=RequestContext(request)
	)

def get_section_report(section):

	if section.attribute == 'genre':
		return get_stats_by_genre(section.questions.all())
	elif section.attribute == 'birth_date':
		return get_stats_by_birth(section.questions.all())
	elif section.attribute == '':
		pass

	elif section.attribute == '':
		pass

	elif section.attribute == 'children':
		return get_stats_by_children(section.questions.all())

	elif section.attribute == 'status':
		return get_stats_by_status(section.questions.all())

	elif section.attribute == 'stratum':
		return get_stats_by_stratum(section.questions.all())

	elif section.attribute == 'role':
		return get_stats_by_role(section.questions.all())

	elif section.attribute == 'semester':
		return get_stats_by_semester(section.questions.all())

	elif section.attribute == 'base':
		return get_stats_by_base(section.questions.all())



