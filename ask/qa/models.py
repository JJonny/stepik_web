from django.contrib.auth.models import User
from django.db import models

SHORT_TITLE_LEN = 66

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
        return '{} - {}'.format(self.id, self.title)

    def get_url(self):
        return '/question/{}/'.format(self.id)

    def get_short_title(self):
        if len(self.title) > SHORT_TITLE_LEN:
            return self.title[:SHORT_TITLE_LEN] + '...'
        else:
            return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    def __str__(self):
        return '{}-{}'.format(self.question.id, self.question.title)


# class User(models.Model):
#     login = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=50)
#     name = models.CharField(max_length=50)
#
#
# class Session(models.Model):
#     key = models.CharField(max_length=50, unique=True)
#     user = models.ForeignKey(User)
#     expires = models.DateTimeField()

