from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from .serializer import UserSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def list(self, request):
        return Response("You don't have access to this webpage.", status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response("You don't have access to this webpage.", status=status.HTTP_400_BAD_REQUEST)


class FacebookLoginView(generics.GenericAPIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        # username = request.data['userID']
        username = request.data['userID']
        password = request.data['userID']
        email = request.data['email']
        user = User.objects.filter(username=username)

        if user.exists():
            token = Token.objects.get(user=user[0])

            return Response({'token': token.key}, status=status.HTTP_200_OK)

        new_user = User.objects.create(
            username=username, password=password, email=email)
        token = Token.objects.create(user=new_user)

        return Response({'token': token.key}, status=status.HTTP_200_OK)
