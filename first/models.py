from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class AdvisorModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)

    class Meta:
        db_table = 'advisors'
        #app_label = 'network'


class BookingAdvisorModel(models.Model):
    advisor_id = models.ForeignKey(
        'Advisormodel', on_delete=models.PROTECT, related_name='booking', db_column='advisor_id')
    booking_time = models.CharField(max_length=255)

    class Meta:
        db_table = 'booking'
        #app_label = 'network'
