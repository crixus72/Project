from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ScrumyGoals(models.model):
    goal_name = models.TextField()
    goal_id = models.IntegerField()
    created_by = models.TextField()
    moved_by = models.TextField()
    owner = models.TextField()
    goal_status = models.ForeignKey(
        'GoalStatus',
        on_delete=models.CASCADE()
    )
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE()
    )

class ScrumyHistory(models.model):
    moved_by = models.TextField
    created_by = models.TextField
    moved_from = models.TextField
    moved_to = models.TextField
    time_of_action = models.DateTimeField

class GoalStatus(models.model):
    status_name = models.TextField()



