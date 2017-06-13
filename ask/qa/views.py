from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Question, Answer
from .forms import AskForm, AnswerForm, LoginForm, SignupForm


def test(request):
    questions = Question.objects.all()
    return render(request, 'blog/home.html', {'questions': questions})

@login_required(login_url='/login/')
def question(request, id):
    current_question = get_object_or_404(Question, pk=id)
    answers = current_question.answer_set.order_by('-added_at')
    if request.method == 'POST':
        form_answer = AnswerForm(request.POST)
        if form_answer.is_valid():
            form_answer.save(request.user)
            return HttpResponseRedirect(current_question.get_url())
    else:
        form_answer = AnswerForm(initial={'question': str(id)})
    return render(request, 'blog/question.html', {
            'question': current_question,
            'form_answer': form_answer,
            'answers': answers,
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
    return render_to_response('blog/home.html',
                              {'page_posts': page_posts,
                               'user': request.user,
                               'session': request.session, })


def about(request):
    return render(request, 'blog/about.html')


@login_required(login_url='/login/')
def new_ask(request):
    if request.method == 'POST':
        forms = AskForm(request.POST)
        if forms.is_valid():
            forms.save(request.user)
            last_id = Question.objects.new()[0].id
            return HttpResponseRedirect('/question/{}/'.format(last_id))
    else:
        forms = AskForm()
    return render(request, 'blog/new.html', {'forms': forms})


@login_required(login_url='/login/')
def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form,
                                               'user': request.user,
                                               'session': request.session, })


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data["username"]
            password = form.raw_password
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'blog/signup.html', {'form': form,
                                           'user': request.user,
                                           'session': request.session, })


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists(),
    }
    return JsonResponse(data)


def rating_up(request):
    post_num = request.GET.get('post_num', None)
    # username = request.GET.get('username', None)
    current_post = get_object_or_404(Question, pk=post_num)
    # user = User.objects.filter(username__iexact=username)
    current_post.rating += 1
    current_post.save()
    data = {
        'rating': current_post.rating,
    }
    return JsonResponse(data)
