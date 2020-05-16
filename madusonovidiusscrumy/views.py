#Django
from django.http import HttpResponse
from madusonovidiusscrumy.models import ScrumyGoals


def get_grading_parameters(request):
    response = ScrumyGoals.objects.filter(goal_name__exact='Learn Django')
    return HttpResponse(response)


# Create your views here.
