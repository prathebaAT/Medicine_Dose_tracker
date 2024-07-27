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
    
 
                                                                                                   

class Dosage(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20)
    notes = models.TextField(blank=True, null=True)
    prescribed_by = models.CharField(max_length=100, blank=True, null=True)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    frequency = models.IntegerField()

    def __str__(self):
        return f"{self.patient} added {self.quantity} {self.unit} of {self.medicine.medicine_name} on {self.date} at {self.time}"

    def calculate_due_date(self):
        try:
            frequency_per_day = int(self.frequency)
            depletion_days = self.medicine.stock // frequency_per_day
            depletion_date = self.date + timedelta(days=depletion_days)
            reminder_date = depletion_date - timedelta(days=3)
            return f"Depletion Date: {depletion_date.strftime('%Y-%m-%d')}", f"Reminder Date: {reminder_date.strftime('%Y-%m-%d')}"
        except ValueError:
            return "Invalid frequency value", "Invalid frequency value"


    def get_due_dates(self):
        depletion_date, reminder_date = self.calculate_due_date()
        return f"Due: {depletion_date}, Reminder: {reminder_date}"