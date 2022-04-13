from rest_framework import serializers
from .models import state_distribution, patient_record, lga_distribution


        
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = state_distribution
        fields = ['id', 'no_infected', 'state']

class LgaSerializer(serializers.ModelSerializer):
    class Meta:
        model = lga_distribution
        fields = ['id', 'no_infected', 'lga_name']
        

class PatientSerializer(serializers.ModelSerializer):
#    state_name = serializers.CharField(source='state.state')
    class Meta:
        model = patient_record
        fields = '__all__'
        


