from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *

# Create your views here.

class CreatePizza(CreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class ListPizza(ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type','size']

class EditPizza(RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
