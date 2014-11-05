#encoding: utf-8

from django import forms
from polls.models import Person


from datetimewidget.widgets import DateWidget


class PersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = '__all__'

		dateTimeOptions = {
			'format': 'dd/mm/yyyy',
			'autoclose': True,
		}

		widgets = {
            #Use localization and bootstrap 3
            'birth_date': DateWidget(
            	attrs={'id':"datePicker"}, 
            	usel10n = True, 
            	bootstrap_version=3,
            	options = dateTimeOptions
            )
        }