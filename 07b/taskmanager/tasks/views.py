from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_400_BAD_REQUEST

from django.contrib.auth import authenticate
from .models import Task
from .serializers import TaskSerializer
from .decorators import define_usage


class NewTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

"""
    Структура API запросов:
    API: GET http://localhost:8000
    All: GET http://localhost:8000/api/
    Select: GET http://localhost:8000/api/1/
    Create: POST http://localhost:8000/api/ + body ('description', 'due', 'user')
    Update: PUT http://localhost:8000/api/1/ + body ('description', 'due', 'user')
    Delete: DELETW http://localhost:8000/api/1/
"""

# URL api/signin/
@define_usage(params={'username': 'String', 'password': 'String'},
              returns={'authenticated': 'Bool', 'token': 'Token String'})
@api_view(['POST'])
@permission_classes((AllowAny,))
def api_signin(request):
    try:
        username = request.data['username']
        password = request.data['password']
    except:
        return Response({'error': 'Please provide correct username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'authenticated': True, 'token': "Token " + token.key})
    else:
        return Response({'authenticated': False, 'token': None})
