from django.contrib import admin
from django.urls import path,include
from . import views
from .views import StaffViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'staff', StaffViewSet)
urlpatterns = [    
    path('',include(router.urls)),
]