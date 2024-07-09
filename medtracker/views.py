from rest_framework import viewsets

from .models import Medicine, Dosage
from .serializers import MedicineSerializer, DosageSerializer


class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class DosageViewSet(viewsets.ModelViewSet):
    queryset = Dosage.objects.all()
    serializer_class = DosageSerializer