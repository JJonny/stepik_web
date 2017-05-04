from django import forms
# from django.forms import ModelForm
# from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(label='Type title your question')
    text = forms.CharField(label='Type your question', widget=forms.Textarea)

    def clean(self):
        pass

    def save(self, user):
        new_q = Question()
        new_q.title = self.cleaned_data['title']
        new_q.text = self.cleaned_data['text']
        new_q.author = user #User.objects.all()[0]
        new_q.save()


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='')
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        pass

    def get_url(self):
        return 'question/{}/'.format(Question.objects.get(pk=self.cleaned_data['question']))

    def save(self, user):
        answer = Answer()
        answer.text = self.cleaned_data['text']
        answer.author = user # User.objects.all()[0]
        answer.question = Question.objects.get(pk=self.cleaned_data['question'])
        answer.save()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Not set username')
        else:
            return username


    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Not set password')
        else:
            return password


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('Wrong username or password')
        if not user.check_password(password):
            raise forms.ValidationError('Worng username or password')


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Не задано имя пользователя')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError('Такой пользователь уже существует')
        except User.DoesNotExist:
            pass
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Не указан адрес электронной почты')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Не указан пароль')
        self.raw_passeord = password
        return make_password(password)

    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user




