from django import forms
# from django.forms import ModelForm
from django.forms.models import ModelForm

from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(label='Type title your question')
    text = forms.CharField(label='Type your question', widget=forms.Textarea)

    def save(self, user):
        new_q = Question()
        new_q.title = self.cleaned_data['title']
        new_q.text = self.cleaned_data['text']
        new_q.author = user
        new_q.save()

    def get_url(self):
        return 'question/' + str(Question.objects.count()) + '/'


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text']

    def clean(self):
        pass

    def get_url(self):
        return 'question/' + str(Question.objects.count()) + '/'

    def save(self, user, id, commit=True):
        answer = Answer()
        answer.text = self.cleaned_data['text']
        answer.question = Question.objects.get(pk=id)
        answer.author = user
        answer.save()
