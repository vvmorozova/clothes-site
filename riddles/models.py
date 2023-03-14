from django.db import models

# Create your models here.
from django.db import models

#riddles
class Riddle(models.Model):
    riddle_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')


class Option(models.Model):
    riddle = models.ForeignKey(Riddle, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

#clothes
class Item(models.Model):
    color = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    style = models.CharField(max_length=255)
    class Gender(models.TextChoices):
        woman = 'w'
        man = 'm'
        uni = 'u'
        girls = 'g'
        boys = 'b'
        uni_kids = 'cu'
    gender = models.TextField(choices=Gender.choices, default=Gender.woman)
    size = models.IntegerField(default=0)

class Pics(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='pics')

#class Sizes(models.Model):
    #item = models.ForeignKey(Item, on_delete=models.CASCADE)
    #size =  models.IntegerField()

class Composition(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    material = models.CharField(max_length=255)
    percent = models.IntegerField(default=0)

import datetime

from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text