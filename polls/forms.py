from django import forms
from polls.models import Count

class CountForm(forms.ModelForm):
    class Meta:
        model = Count
