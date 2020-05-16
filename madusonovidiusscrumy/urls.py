#Django
from django.urls import path

#Local
from . import views

urlpatterns = [
    #path('', views.get_grading_parameters, name='get_grading_parameters'),
    path('<int:goal_id>/', views.move_goal, name='move_goal')
]

