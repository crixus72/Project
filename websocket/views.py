from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ChatMessage, ConnectionModel
# Create your views here.


@csrf_exempt
def test(request):
    return JsonResponse({'message': 'hello Daud'}, status=200)


def __parse__body(body):
    body_unicode = body.decode('utf-8')
    return json.loads(body_unicode)


@csrf_exempt
def connect(request):
    body = __parse__body(request.body)
    connection_id = body['connectionId']
    connection_id.save()
    return JsonResponse({'message': 'Connect Successfully'}, status=200)


def disconnect(request):
    body = __parse__body(request.body)
    connection_id = body['connectionId']
    connection_id.delete()
    return JsonResponse({'message': 'Disconnect Successfully'}, status=200)

