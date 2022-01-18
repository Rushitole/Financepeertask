from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .models import*
from .serializers import FileModelSerializer, PostDataSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import TokenAuthentication


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


# LOGIN

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class PostDataViewSets(viewsets.ReadOnlyModelViewSet):
    # authentication_classes = (TokenAusthentication,)
    queryset = PostData.objects.all()
    serializer_class = PostDataSerializer
    # permission_classes = (IsAuthenticated,)


class FileModelViewSets(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication,)
    queryset = FileModel.objects.all()
    serializer_class = FileModelSerializer
    # permission_classes = (IsAuthenticated,)