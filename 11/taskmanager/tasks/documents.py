from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Task
from .search_indexes import TaskIndex


@registry.register_document
class CarDocument(Document):
    class Index:
        name = 'tasks'
        settings = {'number_of_shards': 1,
    'number_of_replicas': 0}

    class Django:
        model = Task
        fields = ['id', 'user', 'description', 'due']


TaskIndex.init()
