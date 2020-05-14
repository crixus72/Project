from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class GoalStatus(models.Model):
    status_name = models.TextField()


class ScrumyGoals(models.Model):
    goal_name = models.TextField()
    goal_id = models.IntegerField()
    created_by = models.TextField()
    moved_by = models.TextField()
    owner = models.TextField()
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT)
    user = models.ForeignKey('User',
        on_delete=models.CASCADE, related_name='user+',)


class ScrumyHistory(models.Model):
    moved_by = models.TextField
    created_by = models.TextField
    moved_from = models.TextField
    moved_to = models.TextField
    time_of_action = models.DateTimeField
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)


class User(models.Model):
    pass
