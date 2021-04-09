from rest_framework import serializers
from .models import Todo, CheckList


class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = ('id', 'text', 'status', 'todo')


class TodoSerializer(serializers.ModelSerializer):
    checklist = CheckListSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Todo
        fields = ('id', 'memo', 'status', 'checklist', 'user')
        read_only_fields = ('id', 'checklist')
