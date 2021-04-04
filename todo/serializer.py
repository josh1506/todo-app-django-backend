from rest_framework import serializers
from .models import Todo, CheckList


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('memo', 'cover', 'status')


class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = ('text', 'status')
