from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import StateSerializer, PatientSerializer, LgaSerializer
from .models import state_distribution, patient_record, lga_distribution


# Create your views here.

class StateViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = StateSerializer
    queryset = state_distribution.objects.all()
    

    

class PatientViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PatientSerializer
    queryset = patient_record.objects.all()
    
class LgaViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = LgaSerializer
    queryset = lga_distribution.objects.all()

    




