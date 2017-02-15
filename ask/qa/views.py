from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse

from .models import Question
# from .forms import NewQuestionForm


def test(request):
    questions = Question.objects.all()
    return render(request, 'blog/home.html', {'question': questions})


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
