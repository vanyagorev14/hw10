import datetime

from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Person(models.Model):
    first_name = models.CharField(_('first_name'), max_length=120, help_text='Here you must enter name')
    family_name = models.CharField(_('family_name'), max_length=120, help_text='Here you must enter surname')
    email = models.EmailField(_('email_adress'), help_text='You must enter email field')

    def __str__(self):
        return '{0}, {1}'.format(self.first_name, self.family_name)

    def url_return(self):
        return reverse('polls:person-detail', args=[str(self.id)])


class Log(models.Model):
    path = models.FilePathField(max_length=100, help_text="PATH")
    method = models.CharField(max_length=4, help_text='METHOD')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.method} {self.path}'