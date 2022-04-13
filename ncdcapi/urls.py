from django.urls import path, include
from ncdcapi import views 
from rest_framework import routers

from rest_framework.routers import DefaultRouter
from rest_framework import viewsets
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register(r'state', views.StateViewSet, 'state')
router.register(r'patient', views.PatientViewSet, 'patient')
router.register(r'lga', views.LgaViewSet, 'lga')



urlpatterns = [
    path('', include(router.urls)),
    path('openapi/', get_schema_view(
        title="Invoice Service",
        description="API developers hoping to use our service"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='ncdcapi/documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),


]
