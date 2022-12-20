from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes
import json
from django.shortcuts import HttpResponse

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class=StudentSerializer