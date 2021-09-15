from .models import Object
from rest_framework import serializers
from .tasks import send_email
from .models import Object


class ObjectSerializer(serializers.ModelSerializer):
    # def save(self, *args, **kwargs):
    #     send_email()
    #     super(ObjectSerializer, self).save(*args, **kwargs)

    class Meta:
        model = Object
        fields = ('id', 'data')
