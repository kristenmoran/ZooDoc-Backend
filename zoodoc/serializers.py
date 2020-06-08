from rest_framework import serializers
from .models import Doctor, Review


class DoctorSerializer(serializers.HyperlinkedModelSerializer):

    reviews = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Doctor
        fields = ('id', 'first_name', 'last_name', 'gender',
                  'image_url', 'specialization', 'office_name', 'website', 'about', 'street_address', 'city', 'state', 'zip_code', 'phone_number', 'reviews')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    doctor = serializers.HyperlinkedRelatedField(
        view_name='doctor_detail',
        many=False,
        read_only=True
    )

    class Meta:
        model = Review
        fields = ('name', 'description', 'overall_rating',
                  'bed_side_rating', 'wait_time_rating', 'created_at', 'doctor',)
