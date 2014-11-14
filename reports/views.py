from django.http import JsonResponse

from polls.models import Person, Question
from frontend.models import Application, Answer
from django.db.models import Count

# Create your views here.

def create_report(request):
	attribute = request.GET.get('attr')
	question_id = int(request.GET.get('question_id'))

	persons = Person.objects.all()

	if attribute == 'genre':
		return get_stats_by_genre(question_id)


def get_stats_by_genre(question_id):

	question = Question.objects.get(id=question_id)

	male_answers = Answer.objects.filter(
		application__person__genre='M', option__question=question
	).values_list('option__text').order_by().annotate(Count('option__text'))


	female_answers = Answer.objects.filter(
		application__person__genre='F', option__question=question
	).values_list('option__text').order_by().annotate(Count('option__text'))

	print male_answers
	print female_answers    

	value_0 = [2,2,0]
	value_1 = [2,1,0]




    

