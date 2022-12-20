from django.contrib import admin
from django.urls import path,include
from . import views
from .views import ExamViewSet, QuestionViewSet, ScoreViewSet
from rest_framework import routers


router= routers.DefaultRouter()

router.register(r'exam', ExamViewSet)
urlpatterns = [    
    path('',include(router.urls)),
]

router.register(r'question', QuestionViewSet)
urlpatterns = [    
    path('',include(router.urls)),
]

router.register(r'score', ScoreViewSet)
urlpatterns = [    
    path('',include(router.urls)),
]