from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicineViewSet, DosageViewSet


router = DefaultRouter()
router.register(r'medicines', MedicineViewSet)
router.register(r'doses', DosageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]