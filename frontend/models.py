from django.db import models

from polls.models import Person, Poll, Option, Question
# Create your models here.

class Application(models.Model):
	person = models.ForeignKey(Person)
	poll = models.ForeignKey(Poll)
	datetime = models.DateTimeField(auto_now=True)

class Answer(models.Model):
	application = models.ForeignKey(Application)
	option = models.ForeignKey(Option)

	class Meta:
		unique_together = ('application', 'option')	
			
