from django.db import models

# Create your models here.
class state_distribution(models.Model):
    no_infected = models.IntegerField()
    state = models.CharField(max_length=100)
    Latitude_value = models.CharField(max_length=200)
    Latitude_alias = models.CharField(max_length=200)
    Longitude_value	= models.CharField(max_length=200)
    Longitude_alias = models.CharField(max_length=200)
    
    def __str__(self):
        return self.state
    
class lga_distribution(models.Model):
    no_infected = models.IntegerField()
    lga_name = models.CharField(max_length=100)
    Latitude_value = models.CharField(max_length=200)
    Latitude_alias = models.CharField(max_length=200)
    Longitude_value	= models.CharField(max_length=200)
    Longitude_alias = models.CharField(max_length=200)
    
    def __str__(self):
        return self.state

    
GENDER = (
('MALE', 'MALE'),
('FEMALE', 'FEMALE'),
)

class patient_record(models.Model):
    state = models.ForeignKey('state_distribution', on_delete = models.CASCADE, null=True, blank=True)
    health_center = models.CharField(max_length=500)
    doctor_name = models.CharField(max_length=500)
    address = models.TextField()
    ref_no = models.CharField(max_length=100)
    gender = models.CharField(max_length=30, choices=GENDER)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True)
    age = models.IntegerField(default= 0 )
    blood = models.CharField(max_length=10, blank=True)
    cough = models.BooleanField(default=False)
    fever = models.BooleanField(default=False)
    measles = models.BooleanField(default=False)
    rashes = models.BooleanField(default=False)
    red_watery_eye = models.BooleanField(default=False)
    runny_nose = models.BooleanField(default=False)
