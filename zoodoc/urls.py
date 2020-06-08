from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('doctors/', views.DoctorList.as_view(), name='doctor_list'),
    path('doctors/<int:pk>', views.DoctorDetail.as_view(), name='doctor_detail'),
    path('reviews/', views. ReviewList.as_view(),
         name='review_list'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(),
         name='review_detail'),
]
