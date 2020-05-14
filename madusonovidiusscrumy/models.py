from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class GoalStatus(models.Model):
    STATUS_CHOICES=(
        ('pending', 'Pending',),
        ('reviewing', 'Reviewing'),
        ('approval', 'Approval')
    )
    status_name = models.CharField(max_length=15,
                                   choices=STATUS_CHOICES,
                                   default='pending')

    def __str__(self):
        return self.status_name


class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length=50)
    goal_id = models.IntegerField(default=1)
    created_by = models.CharField(max_length=50)
    moved_by = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT)
    user = models.ForeignKey(User,
                             on_delete=models.PROTECT,
                             related_name='goal_created',)

    def __str__(self):
        return self.goal_name


class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)
    moved_from = models.CharField(max_length=50)
    moved_to = models.CharField(max_length=50)
    time_of_action = models.DateTimeField(default=timezone.now)
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by
