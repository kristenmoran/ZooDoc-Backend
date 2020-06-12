from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegistrationAPIView, LoginAPIView
from . import views

app_name = 'users'
urlpatterns = [
    path('users/register', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
