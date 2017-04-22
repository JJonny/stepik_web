from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.contrib.auth.decorators import login_required
# from mysql.connector import authentication

from .models import Question
from .forms import AskForm, AnswerForm


def test(request):
    questions = Question.objects.all()
    return render(request, 'blog/home.html', {'questions': questions})


def question(request, id):
    current_question = get_object_or_404(Question, pk=id)
    if request.method == 'POST':
        form_answer = AnswerForm(request.POST)
        if form_answer.is_valid():
            form_answer.save()
            return HttpResponseRedirect(current_question.get_url())
    else:
        form_answer = AnswerForm(initial={'question': str(id)})
    return render(request, 'blog/question.html', {
            'question': current_question,
            'form_answer': form_answer,
        })


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


#@login_required
def new_ask(request):
    if request.method == 'POST':
        forms = AskForm(request.POST)
        if forms.is_valid():
            forms.save()
            last_id = Question.objects.new()[0].id
            print('-----count after save {}', last_id)
            return HttpResponseRedirect('/question/{}/'.format(last_id))
    else:
        forms = AskForm()
    return render(request, 'blog/new.html', {'forms': forms})

#
# #@login_required
# def new_answer(request):
#     if request.method == 'POST':
#         forms = AnswerForm(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return HttpResponseRedirect('/') # need question redirect to page
#     else:
#         forms = AnswerForm()
#     return render(request, 'blog/answer.html', {'forms': forms})
