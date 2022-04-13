from django.urls import path, include
from ncdcapi import views 
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework import viewsets


router = routers.DefaultRouter()
router.register(r'state', views.StateViewSet, 'state')
router.register(r'patient', views.PatientViewSet, 'patient')
router.register(r'lga', views.LgaViewSet, 'lga')



urlpatterns = [
    path('', include(router.urls)),
]
