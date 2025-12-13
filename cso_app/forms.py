from django import forms
from .models import CSOEvent

class CSOEventForm(forms.ModelForm):
    class Meta:
        model = CSOEvent
        fields = [
            'location',
            'latitude',
            'longitude',
            'start_time',
            'end_time',
            'overflow_volume_m3',
            'cause',
            'severity',
            'description',
        ]
