from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicineViewSet, DosageViewSet, UserViewSet, UserViewSet, RegisterView, LoginView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_nested.routers import NestedDefaultRouter

router = DefaultRouter()
router.register(r'medicines', MedicineViewSet)
router.register(r'users', UserViewSet)

medicines_router = NestedDefaultRouter(router, r'medicines', lookup='medicine')
medicines_router.register(r'dosages', DosageViewSet, basename='medicine-dosages')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(medicines_router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]