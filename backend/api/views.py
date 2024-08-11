from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from api.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = User
    permission_classes = [AllowAny]
