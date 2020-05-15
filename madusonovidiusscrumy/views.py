#Django
from django.shortcuts import render
from django.http import HttpResponse
from madusonovidiusscrumy.models import GoalStatus


# Create your views here.
def get_grading_parameters(request):
    result = GoalStatus.objects.filter(status_name__exact='Weekly Goal')
    return HttpResponse(result)
