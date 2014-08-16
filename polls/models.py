from django.db import models
import datetime
from django.utils import timezone

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now = True)
    def __unicode__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.choice

class Human(models.Model):
    name = models.CharField(max_length=12)
    description = models.TextField()
    age = models.IntegerField()
    def __unicode__(self):
        return self.name

class Count(models.Model):
    num = models.IntegerField()
