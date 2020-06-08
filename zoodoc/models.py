from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=25)
    specialization = ArrayField(models.CharField(
        max_length=100), null=True, blank=True)
    image_url = models.TextField()

    about = models.TextField()
    office_name = models.CharField(max_length=50)
    website = models.TextField()
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=25)

    def __str__(self):
        return self.first_name


class Review(models.Model):

    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    name = models.CharField(max_length=50)
    description = models.TextField()
    overall_rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    bed_side_rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    wait_time_rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    created_at = models.DateTimeField()
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.name
