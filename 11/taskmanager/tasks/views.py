from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework_elasticsearch import es_views, es_filters
from elasticsearch import Elasticsearch, RequestsHttpConnection

from django.contrib.auth import authenticate
from .models import Task
from .serializers import TaskSerializer
from .decorators import define_usage
from .search_indexes import TaskIndex


class NewTaskViewSet(viewsets.ModelViewSet):
    """Структура API запросов:
    API: GET http://localhost:8000
    All: GET http://localhost:8000/api/
    Select: GET http://localhost:8000/api/1/
    New: POST http://localhost:8000/api/ + body ('description', 'due', 'user')
    Update: PUT http://localhost:8000/api/1/ + body ('description', 'due', 'user')
    Delete: DELETW http://localhost:8000/api/1/
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

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


class BlogView(es_views.ListElasticAPIView):
    es_client = Elasticsearch(hosts=['elasticsearch:9200/'],
                              connection_class=RequestsHttpConnection)
    es_model = TaskIndex
    es_filter_backends = (
        es_filters.ElasticFieldsFilter,
        es_filters.ElasticSearchFilter
    )
    es_filter_fields = (
        es_filters.ESFieldFilter('tag', 'tags'),
    )
    es_search_fields = (
        'tags',
        'title',
    )