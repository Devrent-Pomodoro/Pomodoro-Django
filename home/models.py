from django.db import models
from django.contrib.auth.models import User

class StudyTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.IntegerField()  # total study minute in that day

