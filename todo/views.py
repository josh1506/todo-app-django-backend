from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import CheckListSerializer, TodoSerializer
from .models import Todo, CheckList


class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
