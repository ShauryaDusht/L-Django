from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MoviedataSerializer
from .models import Moviedata
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all().order_by('name')
    serializer_class = MoviedataSerializer
    
class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all().filter(genre='action').order_by('name')
    serializer_class = MoviedataSerializer
    

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all().filter(genre='comedy').order_by('name')
    serializer_class = MoviedataSerializer

