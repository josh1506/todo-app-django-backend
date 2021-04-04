from rest_framework import serializers
from .models import Todo, CheckList


class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = ('id', 'text', 'status')


class TodoSerializer(serializers.ModelSerializer):
    checklist = CheckListSerializer(many=True)

    class Meta:
        model = Todo
        fields = ('memo', 'cover', 'status', 'checklist')
