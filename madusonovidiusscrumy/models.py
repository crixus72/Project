from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ScrumyGoals(models.model):
    goal_name = models.CharField()
    goal_id = models.IntegerField()
    created_by = models.CharField()
    moved_by = models.CharField()
    owner = models.CharField()
    goal_status = models.ForeignKey('GoalStatus', on_delete=models.PROTECT())
    user = models.ForeignKey('User', on_delete=models.CASCADE())


class ScrumyHistory(models.model):
    moved_by = models.CharField
    created_by = models.CharField
    moved_from = models.CharField
    moved_to = models.CharField
    time_of_action = models.DateTimeField
    goal = models.ForeignKey(ScrumyGoals)


class GoalStatus(models.model):
    status_name = models.CharField()



