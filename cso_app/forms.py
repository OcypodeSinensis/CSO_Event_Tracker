from django import forms
from .models import CSOEvent
from .models import MitigationAction

class MitigationActionForm(forms.ModelForm):
    class Meta:
        model = MitigationAction
        fields = ['cso_event', 'action_type', 'completion_date', 'notes']
        widgets = {
            'completion_date': forms.DateInput(attrs={'type': 'date'}),
        }

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
