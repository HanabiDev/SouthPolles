#encoding: utf-8

from django.contrib import admin
from models import Person, Poll, PollSection, Question, Option
from frontend.models import Application, Answer

class PersonAdmin(admin.ModelAdmin):
    pass

class PollAdmin(admin.ModelAdmin):
    pass

class SectionAdmin(admin.ModelAdmin):
    pass

class QuestionAdmin(admin.ModelAdmin):
    pass

class OptionAdmin(admin.ModelAdmin):
    pass

    def __unicode__(self):
		return 'Pregunta ' + str(self.question.index) + ' > ' + self.text


admin.site.register(Person, PersonAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(PollSection, SectionAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)


class ApplicationAdmin(admin.ModelAdmin):
    pass

class AnswerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Answer, AnswerAdmin)