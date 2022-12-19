from django.db import models

# Create your models here.
from accounts.models import User


class Accommodation(models.Model):
    PAYMENT_METHOD = (
        (1, 'Free'),
        (2, 'Fixed Price'),
        (3, 'Any Amount'),
    )

    name = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    city = models.CharField(max_length=200)
    num_of_guests = models.IntegerField(max_length=200)
    address = models.CharField(max_length=1000)
    day_available = models.CharField(max_length=200)
    payment_method = models.PositiveSmallIntegerField(choices=PAYMENT_METHOD)

    def __str__(self):
        return self.name


class Booking(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_of_guests = models.IntegerField(max_length=200)
    first_day = models.CharField(max_length=200)
    last_day = models.CharField(max_length=80)

    def __str__(self):
        return f'Booking done by {self.user.first_name} on {self.accommodation.name}. '
