from django import forms

from core.models import Accommodation


class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        exclude = ['user']
