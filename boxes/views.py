from django.shortcuts import render
from rest_framework import generics

from .models import Box
from .serializers import BoxSerializer

# Create your views here.
class BoxListCreateView(generics.ListCreateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer


class BoxDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer