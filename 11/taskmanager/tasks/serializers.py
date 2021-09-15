from rest_framework import serializers
from rest_framework_elasticsearch.es_serializer import ElasticModelSerializer
from .models import Task
from .search_indexes import TaskIndex


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'description', 'due', 'user')


class ElasticBlogSerializer(ElasticModelSerializer):
    class Meta:
        model = Task
        es_model = TaskIndex
        fields = ('id', 'description', 'due', 'user')