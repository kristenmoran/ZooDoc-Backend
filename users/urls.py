from django.urls import path, include
from .views import RegistrationAPIView, LoginAPIView
from . import views

app_name = 'users'
urlpatterns = [
    path('users/register', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()), ]
