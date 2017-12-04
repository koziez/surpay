import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    text = models.CharField(max_length=200)
    date_made = models.DateTimeField(auto_now_add=True, blank=True)
    votes = models.IntegerField(default=0)

    def was_published_recently(self):
        return self.date_made >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    percentage = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.text

class Vote(models.Model):
    session_key = models.CharField(max_length=40, default="")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    date_made = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.choice.text
