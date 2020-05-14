#Django
from django.urls import path

#Local
from . import views

urlpatterns = [
    path('', views.get_grading_parameters),
]

