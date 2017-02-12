from django.shortcuts import render

# Create your views here.
from qa.models import Question

# import os
#
#
# def question(req, id):
#     file = req.GET.get('fil')
#     if file == 'gf':
#         file += os.path.abspath(__file__)
#
#     ss = 'Your request consist ' + str(id) + file
#
#     post = {
#             'title': 'Answer',
#             'text': 'OK',
#             'str': ss
#             }
#     return render(req, 'base/base.html', {
#         'post': post
#     })


def test(request, *args, **kwargs):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'blog/home.html', context)


def about(request, *args, **kwargs):
    return render(request, 'blog/about.html')
