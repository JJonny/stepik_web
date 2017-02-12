from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
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
    return HttpResponse("OK")
