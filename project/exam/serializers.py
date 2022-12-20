from .models import Exam, Question, Score
from rest_framework import serializers

class ExamSerializer(serializers.ModelSerializer):
	class Meta:
		model=Exam
		fields="__all__"

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model=Question
		fields="__all__"

class ScoreSerializer(serializers.ModelSerializer):
	class Meta:
		model=Score
		fields="__all__"