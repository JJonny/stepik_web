from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from mysql.connector import authentication

from .models import Question, Answer
from .forms import AskForm, AnswerForm


def test(request):
    questions = Question.objects.all()
    return render(request, 'blog/home.html', {'questions': questions})


def question(request, id):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save(request.user, id)
            return HttpResponseRedirect(form.get_url())

    else:
        current_question = get_object_or_404(Question, pk=id)
        answers = Answer.objects.filter(question=id)
        form = AnswerForm()
        data = {
            'question': current_question,
            'answers': answers,
            'forms': form,
        }
    return render(request, 'blog/question.html', data)


def popular(request):
    questions = Question.objects.popular()
    paginator = Paginator(questions, 10)
    page = request.GET.get('page')
    try:
        page_posts = paginator.page(page)
    except PageNotAnInteger:
        page_posts = paginator.page(page)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/popular.html', {'page_posts': page_posts})


def listing(request):
    post_all = Question.objects.new()
    paginator = Paginator(post_all, 10)
    page = request.GET.get('page')
    try:
        page_posts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_posts = paginator.page(page)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)
    return render_to_response('blog/home.html', {'page_posts': page_posts})


def about(request):
    return render(request, 'blog/about.html')


@login_required
def new_ask(request):
    if request.method == 'POST':
        forms = AskForm(request.POST)
        if forms.is_valid():
            forms.save(request.user)
            return HttpResponseRedirect('/' + forms.get_url())
    else:
        forms = AskForm()
    return render(request, 'blog/new.html', {'forms': forms})


@login_required
def new_answer(request):
    if request.method == 'POST':
        forms = AnswerForm(request.POST)
        if forms.is_valid():
            forms.save(request.user)
            return HttpResponseRedirect('/') # need question redirect to page
    else:
        forms = AnswerForm()
    return render(request, 'blog/answer.html', {'forms': forms})
