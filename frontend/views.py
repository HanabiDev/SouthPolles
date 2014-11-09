#encoding: utf-8

from django.shortcuts import redirect, render_to_response 
from forms import PersonForm
from django.template import RequestContext
from django.core.urlresolvers import reverse
from models import Application, Answer
from polls.models import Person, Poll, PollSection, Option, Municipio
from django.views.decorators.cache import cache_control


# Create your views here.

def home(request):
	request.session.flush()
	return render_to_response('index.html', request.session)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register_person(request):
	if request.method == 'GET':
		form = list(PersonForm())
		return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))

	if request.method == 'POST':
		form = PersonForm(request.POST)

		if form.is_valid():
			person = form.save()
			request.session['person_id'] = person.id
			return redirect(reverse('list_polls'))
		form = list(form)
		return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def list_polls(request):

	polls = Poll.objects.all()

	return render_to_response(
		'select_poll.html', 
		{'polls': polls},
		context_instance=RequestContext(request)
	)	

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def load_poll(request):

	poll_id = int(request.POST.get('poll_id'))
	poll = Poll.objects.get(id=poll_id)

	new_application = Application.objects.create(
		person = Person.objects.get(id=request.session['person_id']),
		poll = poll,
	);

	request.session['application_id'] = new_application.id
	request.session['saved_sections'] = ()

	return render_to_response('start_poll.html', 
		{'application': new_application, 'poll':new_application.poll}, 
		context_instance=RequestContext(request)
	)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def serve_section(request, section_id):

	if section_id in request.session['saved_sections']:
		section_id = request.session['saved_sections'][-1]

		return redirect(reverse('serve_section', args=(int(section_id)+1,)))

	application = Application.objects.get(id=request.session['application_id'])
	poll_id = application.poll.id
	
	section = None
	try:
		section = PollSection.objects.get(poll__id=poll_id, index=section_id)
	except Exception, e:
		pass

	if not section:
		return redirect(reverse('thanks'))
	

	return render_to_response('poll_section.html', 
		{'section':section, 'section_index': section_id, 'application': application}, 
		context_instance=RequestContext(request)
	)

#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def save_section(request, section_id):

	application = Application.objects.get(id=request.session['application_id'])

	ids = request.POST.getlist('section_'+section_id+'_answers')

	if section_id == '1':
		item_4_option = Option.objects.get(question__index=4, index=1)
		item_5_option = Option.objects.get(question__index=5, index=1)

		if int(ids[3])==item_4_option.id and int(ids[4])==item_5_option.id:

			for option_id in ids:
				option = Option.objects.get(id=option_id)
				try:
					new_answer = Answer.objects.create(application=application, option=option)
				except Exception, e:
					pass

			options = Option.objects.filter(question__poll=application.poll, index=1).exclude(id__in=ids)

			for option in options:
				try:
					new_answer = Answer.objects.create(application=application, option=option)
				except Exception, e:
					pass

			return redirect(reverse('thanks'))

	saved_answers = True
	for option_id in ids:
		option = Option.objects.get(id=option_id)
		try:
			new_answer = Answer.objects.create(application=application, option=option)
		except Exception, e:
			saved_answers = False

	if saved_answers:
		saved_sections = request.session['saved_sections']
		saved_sections.append(section_id) 
		request.session['saved_sections'] = saved_sections

	return redirect(reverse('serve_section', args=(int(section_id)+1,)))






@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def thanks(request):
	return render_to_response('thanks.html', request.session)

@cache_control(no_cache=True, must_revalidate=True)
def dispose_info(request):
	return render_to_response('index.html', request.session)