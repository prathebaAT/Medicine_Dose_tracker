from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicineViewSet, DosageViewSet, UserViewSet, UserViewSet, RegisterView, LoginView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'medicines', MedicineViewSet)
router.register(r'doses', DosageViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]