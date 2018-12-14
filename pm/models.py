from django.db import models
from django.contrib.auth.models import User

class Teams(models.Model):
    team = models.CharField(max_length=50);

    def __str__(self):
        return self.team;

class Tracks(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    track = models.CharField(max_length=50);

    def __str__(self):
        return self.track;

class Users(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    track = models.ForeignKey(Tracks, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Metrics(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    track = models.ForeignKey(Tracks, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    sprint = models.IntegerField();
    startDate = models.DateField();
    endDate = models.DateField();
    devStories = models.IntegerField();
    devStoryPoints = models.IntegerField();
    devCommits = models.IntegerField();
    qaStories = models.IntegerField();
    qaStoryPoints = models.IntegerField();
    qaCommits = models.IntegerField();
