from django.contrib import admin

# Register your models here.
from .models import Accommodation, Booking

admin.site.register(Accommodation)
admin.site.register(Booking)
