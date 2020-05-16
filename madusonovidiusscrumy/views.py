#Django
from django.http import HttpResponse
from madusonovidiusscrumy.models import ScrumyGoals


#def get_grading_parameters(request):
    #response = ScrumyGoals.objects.filter(goal_name__exact='Learn Django')
    #return HttpResponse(response)


def move_goal(request, goal_id):
    answer = ScrumyGoals.objects.get(id=goal_id)
    return HttpResponse(answer)

# Create your views here.
