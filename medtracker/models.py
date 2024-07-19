from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime



class Medicine(models.Model):
    medicine_name = models.CharField(max_length=100)
    composition = models.TextField(blank = True, null = True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    dosage_form = models.CharField(max_length=50, blank=True, null=True)
    expiration_date =models.DateField(blank=True, null=True)
    stock = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.medicine_name
    
    def calculate_due_date():
        pass

class Dosage(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20)
    notes = models.TextField(blank=True, null=True)
    prescribed_by = models.CharField(max_length=100, blank=True, null=True)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    frequency = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.patient} added {self.quantity} {self.unit} of {self.medicine.medicine_name} on {self.date} at {self.time}"