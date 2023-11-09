from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64, unique=True)
    display_name = models.CharField(max_length=64)
    creation_time = models.DateTimeField(auto_now_add=True)
    

class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128)
    creation_time = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='teams')
  

class Board(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    creation_time = models.DateTimeField(auto_now_add=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)  # Use choices for OPEN or CLOSED

class Task(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    creation_time = models.DateTimeField(auto_now_add=True)
    user_assigned = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)  # Use choices for OPEN, IN_PROGRESS, or COMPLETE
