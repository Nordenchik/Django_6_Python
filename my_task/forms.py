from django import forms
from django.forms import ModelForm

from .models import Task

class TaskImageInput(forms.FileInput):
    template_name = 'widgets/task_image.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['has_existing_image'] = bool(value)
        context['widget']['existing_image_name'] = value.name if value else ''
        return context

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
        fields = ['name', 'description', 'image', 'status', 'priority', 'progress_termin']
        widgets = {
            'description': forms.Textarea(
                attrs={'placeholder': 'Опишіть завдання.'}
            ),
            'image': TaskImageInput(
                attrs={
                    'accept': 'image/*',
                    'class': 'd-none task-image-input',
                },
            ),
        }
