from django.shortcuts import render
from rest_framework import viewsets
from .models import Exam, Question, Score
from .serializers import ExamSerializer, QuestionSerializer, ScoreSerializer
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes
import json
from django.shortcuts import HttpResponse

# Create your views here.
class ExamViewSet(viewsets.ModelViewSet):
    queryset= Exam.objects.all()
    serializer_class=ExamSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset= Question.objects.all()
    serializer_class=QuestionSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    queryset= Score.objects.all()
    serializer_class=ScoreSerializer