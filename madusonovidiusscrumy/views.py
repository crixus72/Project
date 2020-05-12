#Django
from django.http import HttpResponse


# Create your views here.
def get_grading_parameters(request):
    return HttpResponse("This is a Scrum application")
