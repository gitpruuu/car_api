from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: User
        fields = ['url', 'username', 'email', 'groups']

class CarModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: Group
        fields:['id', 'name']

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: Group
        fields:['id', 'model', 'color', 'year']
