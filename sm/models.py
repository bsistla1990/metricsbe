from django.db import models
from django.contrib.auth.models import User
from pm.models import Users
from pm.models import Teams
from pm.models import Tracks

class Sprint(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    track = models.ForeignKey(Tracks, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    sprint = models.IntegerField();
    startDate = models.DateField();
    endDate = models.DateField();
    activity = models.CharField(max_length=50)
    story = models.CharField(max_length=10)
    points = models.IntegerField()

class UpsDowns(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    track = models.ForeignKey(Tracks, on_delete=models.CASCADE)
    sprint = models.IntegerField();
    startDate = models.DateField();
    endDate = models.DateField();
    type = models.CharField(max_length=300)
    val = models.CharField(max_length=300)