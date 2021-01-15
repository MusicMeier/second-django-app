from django.shortcuts import render
from rest_framework import viewsets
from .models import Bear
from .serializers import BearSerializer

# Create your views here.
class BearView(viewsets.ModelViewSet):
  queryset = Bear.objects.all()
  serializer_class = BearSerializer