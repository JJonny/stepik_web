from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    def __str__(self):
        return self.title

    class QuestionManger:
        def new(self):
            pass

        def popular(self):
            pass


# class Likes(models.Model):
#     question = models.ForeignKey(Question, related_name='like_question')
#     user = models.ForeignKey(User, related_name='like_user')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
