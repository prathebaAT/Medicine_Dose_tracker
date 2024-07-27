from django.contrib import admin
from .models import  Medicine, Dosage




class DosageAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'patient', 'date', 'time', 'quantity', 'unit', 'get_due_dates')
    
    def get_due_dates(self, obj):
        return obj.get_due_dates()
    get_due_dates.short_description = 'Due Dates'

admin.site.register(Medicine)
admin.site.register(Dosage,DosageAdmin)
