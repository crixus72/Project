# Django
from django.http import HttpResponse
from madusonovidiusscrumy.models import *
from django.contrib.auth.models import User
from random import randint


# def get_grading_parameters(request):
# response = ScrumyGoals.objects.filter(goal_name__exact='Learn Django')
# return HttpResponse(response)


def move_goal(request, goal_id):
    answer = ScrumyGoals.objects.get(id=goal_id)
    return HttpResponse(answer)


def add_goal(request):
    already_used = []
    number = randint(1000, 9999)
    if number not in already_used:
        addgoal = ScrumyGoals.objects.create(goal_name='Keep Learning Django',
                                             goal_id=number,
                                             created_by='Louis',
                                             moved_by='Louis', owner='Louis',
                                             goal_status=GoalStatus.objects.get
                                             (status_name='Weekly Goal'),
                                             user=User.objects.get(
                                                 username='Louis Oma')
                                             )
        already_used.append(number)
    return HttpResponse(addgoal)

def home (request):
    show_record = ScrumyGoals.objects.filter(goal_name__exact=
                                             'Keep Learning Django')
    output = ', '.join([a.goal_name for a in show_record])
    return HttpResponse(output)

# Create your views here.
