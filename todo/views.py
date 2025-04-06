from django.shortcuts import render
from rest_framework import viewsets
from .models import*
from .serializers import *

# Create your views here.

class todoviewset(viewsets.ModelViewSet):
    queryset=todos.objects.all()
    serializer_class=todoitem
