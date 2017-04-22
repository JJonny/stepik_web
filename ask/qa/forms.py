from django import forms
# from django.forms import ModelForm
# from django.forms.models import ModelForm
from django.contrib.auth.models import User

from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(label='Type title your question')
    text = forms.CharField(label='Type your question', widget=forms.Textarea)

    def clean(self):
        pass

    def save(self):
        new_q = Question()
        new_q.title = self.cleaned_data['title']
        new_q.text = self.cleaned_data['text']
        new_q.author = User.objects.all()[0]
        new_q.save()


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='')
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        pass

    def get_url(self):
        return 'question/{}/'.format(Question.objects.get(pk=self.cleaned_data['question']))

    def save(self):
        answer = Answer()
        answer.text = self.cleaned_data['text']
        answer.author = User.objects.all()[0]
        answer.question = Question.objects.get(pk=self.cleaned_data['question'])
        answer.save()
