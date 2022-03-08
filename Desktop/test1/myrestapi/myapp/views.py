from django.shortcuts import render
from rest_framework import viewsets
from .serializers import studentserializers
from .models import student
# Create your views here.
class studentviewset(viewsets.ModelViewSet):
    queryset = student.objects.all().order_by('firstname')
    serializer_class = studentserializers