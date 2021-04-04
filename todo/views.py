from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializer import CheckListSerializer, TodoSerializer
from .models import Todo, CheckList


class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['GET'])
    def get_user_data(self, request):
        todo_list = [self.serializer_class(
            todo).data for todo in Todo.objects.filter(user=request.user)]

        return Response(todo_list, status=status.HTTP_200_OK)


class CheckListView(viewsets.ModelViewSet):
    queryset = CheckList.objects.all()
    serializer_class = CheckListSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, pk):
        task = CheckList.objects.get(id=pk)
        todo = Todo.objects.filter(id=task.todo.pk, user=request.user)

        if not todo.exists():
            return Response({'error': 'Todo not found'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        task.text = request.data['text']
        task.status = request.data['status']
        task.save()

        return Response('Saved', status=status.HTTP_200_OK)
