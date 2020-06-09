from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import boto3
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


def _send_to_connection(connection_id, data):
    gatewayapi = boto3.client('apigatewaymanagementapi',
                              endpoint_url='https://ht8g1d3d53.execute-api.us-east-2.amazonaws.com/teststage',
                              region_name='us-east-2b',
                              aws_access_key_id='AKIAVRTQC3NKDTP7YONO',
                              aws_secret_access_key='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'
                              )
    return gatewayapi.post_to_connection(ConnectionId=connection_id,
                                         Data=json.dumps(data).encode('utf-8'))


def send_message(request):
    body = __parse__body(request.body)
    text = ChatMessage.objects.create(
        username=['body']["username"],
        timestamp=['body']["username"],
        message=['body']["username"],
    )
    connections = ConnectionModel.objects.all()
    data = {'messages': [body]}
    for connection in connections:
        _send_to_connection(connection, data)