from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from .serializers import DoctorSerializer, ReviewSerializer
from rest_framework.permissions import AllowAny,  IsAuthenticated
from .models import Doctor, Review
# Create your views here.


class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['zip_code', 'specialization','city']
    # permission_classes = (AllowAny)


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    # permission_classes = (IsAuthenticated,)


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)
