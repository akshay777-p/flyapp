from django import forms
from .models import Route

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['source', 'destination', 'position', 'duration']

class SearchForm(forms.Form):
    DIRECTION_CHOICES = [
        ('Left', 'Left'),
        ('Right', 'Right'),
    ]
    start_airport = forms.CharField(max_length=5)
    direction = forms.ChoiceField(choices=DIRECTION_CHOICES)
    n = forms.IntegerField(label="Nth Node")
