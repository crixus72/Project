from django.contrib import admin
from .models import ScrumyHistory, ScrumyGoals, GoalStatus

# Register your models here.
admin.site.register(GoalStatus)
admin.site.register(ScrumyGoals)
admin.site.register(ScrumyHistory)

