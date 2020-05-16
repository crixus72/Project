from django.db import models

# Create your models here.
class GoalStatus(model.Model):
status_name = models.CharField(max_length=50)


class ScrumyGoals(models.Model):
	goal_name = models.CharField(max_length=250)
	goal_id = models.IntegerField
	created_by = models.


class ScrumyHistory(models.Model):




