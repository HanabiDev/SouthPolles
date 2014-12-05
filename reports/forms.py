from django import forms
from models import Report, ReportSection

class ReportForm(forms.ModelForm):
	class Meta:
		model = Report
		exclude = ['report_date',]

class ReportSectionForm(forms.ModelForm):
	class Meta:
		model = ReportSection
		exclude = ['diagnostic',]