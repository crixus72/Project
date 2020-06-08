# Django
from django.urls import path

# Local
from websocket import views

app_name = 'websocket'

urlpatterns = [
    path('test/', views.test, name='test'),
    path('disconnect/', views.disconnect, name='disconnect'),
]