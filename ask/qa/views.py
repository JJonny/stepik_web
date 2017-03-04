from django.shortcuts import render, render_to_response, get_object_or_404
# from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Question
# from .forms import NewQuestionForma


def test(request):
    questions = Question.objects.all()
    return render(request, 'blog/home.html', {'questions': questions})


def post_view(request, id):
    # question = Question.objects.get(pk=id)
    question = get_object_or_404(Question, pk=id)
    return render(request, 'blog/question.html', {'question': question})


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


# def add_question(request):
#     return HttpResponse('ok')


# def new_page(request):
#     if request.method == 'POST':
#         forms = NewQuestionForm(request.POST)
#         if forms.is_valid():
#             new_questions = Question()
#             new_questions.title = forms.question
#             new_questions.text = forms.text
#             new_questions.rating = 0
#             new_questions.author = request.user
#             new_questions.likes = request.user
#             new_questions.seve()
#             return HttpResponseRedirect('blog/about.html')
#     else:
#         forms = NewQuestionForm()
#     return render(request, 'blog/new.html', {'forms': forms})
