from djongo import models as djongo_models
from django.db import models

class User(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

class Team(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)

class Activity(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Leaderboard(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
