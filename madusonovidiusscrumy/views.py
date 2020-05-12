#Django
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def get_grading_parameters(request):
    return HttpResponse("<h1>This is a Scrum application</h1>")
