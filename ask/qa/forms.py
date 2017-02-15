from django import forms
from .models import Question


class NewQuestionForm(forms.Form):
	question = forms.CharField(label='Ask people')
	text = forms.CharField(label='Ask your question', widget=forms.Textarea)
