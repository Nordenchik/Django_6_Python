from django import forms
from django.forms import ModelForm

from .models import Task


class TaskForm(ModelForm):
    progress_termin = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={'placeholder': 'DD/MM/YYYY'}
        ),
        required=False,
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'priority', 'progress_termin']
