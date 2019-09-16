from django import forms
from .models import tasks

class taskform(forms.ModelForm):
    class Meta:
        model = tasks
        fields = '__all__'
    