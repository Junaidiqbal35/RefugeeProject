from django import forms

from core.models import Accommodation, Booking


class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        exclude = ['user']


class UpdateAccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = ['day_available', 'available']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['user', 'accommodation']
