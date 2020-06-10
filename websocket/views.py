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


def _parse_body(body):
    body_unicode = body.decode('utf-8')
    return json.loads(str(body_unicode))


@csrf_exempt
def connect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']
    connectionid = ConnectionModel.objects.create(connection_id=connection_id)
    connectionid.save()
    return JsonResponse({'message': 'Connect Successfully'}, status=200)

@csrf_exempt
def disconnect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']
    connectionid = ConnectionModel.objects.get(connection_id=connection_id)
    connectionid.delete()
    return JsonResponse({'message': 'Disconnect Successfully'}, status=200)

@csrf_exempt
def _send_to_connection(connection_id, data):
    gatewayapi = boto3.client('apigatewaymanagementapi',
                              endpoint_url="https://ht8g1d3d53.execute-api.us-east-2.amazonaws.com/teststage",
                              region_name="us-east-2",
                              aws_access_key_id="AKIAJM44KNHZY44QFVKA",
                              aws_secret_access_key="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"
                              )
    return gatewayapi.post_to_connection(ConnectionId=connection_id,
                                         Data=json.dumps(data).encode('utf-8'))

@csrf_exempt
def send_message(request):
    body = _parse_body(request.body)
    text = ChatMessage.objects.create(
        username=body['body']['username'],
        timestamp=body['body']['timestamp'],
        message=body['body']['message'],
    )
    text.save()
    connections = ConnectionModel.objects.all()
    data = {'message': [body]}
    for connection in connections:
        _send_to_connection(connection.connection_id, data)
        print(connection)
    return JsonResponse({'message': 'message sent successfully'}, status=200)


def recent_messages(request):
    connections = ConnectionModel.objects.all()
    messages = [ChatMessage.objects.all()]

    for connection in connections:
        print(sorted(messages))
