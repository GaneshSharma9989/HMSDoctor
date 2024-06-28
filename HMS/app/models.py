# models.py
from django.db import models
 
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    experience = models.IntegerField()
    specialty = models.CharField(max_length=100)
    availability = models.CharField(max_length=10)
    img = models.ImageField(upload_to='doctors/', blank=True, null=True)
