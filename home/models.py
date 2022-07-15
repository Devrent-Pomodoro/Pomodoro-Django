from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudyTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.IntegerField()  # total study minute in that day

class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timerLimit = models.IntegerField()  # minute
    totalStudyTime = models.IntegerField()  # minute
