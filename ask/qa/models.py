from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.ForeignKey(User)

    # likes = models.

    def __str__(self):
        return self.title


# class QuestionManger(models.Model):


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
