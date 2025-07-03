from django import forms
from .models import HealthEntry

class HealthEntryForm(forms.ModelForm):
    class Meta:
        model = HealthEntry
        fields = ['date', 'weight', 'notes']
