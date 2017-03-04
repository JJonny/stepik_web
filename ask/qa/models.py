from django.contrib.auth.models import User
from django.db import models


SHORT_TEXT = 500


class QuestionManger(models.Manager):
    def new(self):
        return Question.objects.order_by('-added_at')

    def popular(self):
        return Question.objects.order_by('-rating')


class Question(models.Model):
    objects = QuestionManger()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT:
            return self.text[:SHORT_TEXT]
        else:
            return self.text


# class Likes(models.Model):
#     question = models.ForeignKey(Question, related_name='like_question')
#     user = models.ForeignKey(User, related_name='like_user')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
