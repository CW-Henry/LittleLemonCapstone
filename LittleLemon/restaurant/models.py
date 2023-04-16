from django.db import models
from django.core.validators import MaxLengthValidator
# Create your models here.


class Menu(models.Model):
    id = models.PositiveIntegerField(
        primary_key=True, max_length=5)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(max_length=5)


class Booking(models.Model):
    id = models.PositiveIntegerField(
        primary_key=True, max_length=11)
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField(
        max_length=6)
    booking_date = models.DateTimeField()
