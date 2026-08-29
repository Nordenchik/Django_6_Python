from django.test import TestCase

from .forms import TaskForm


class TaskFormDateFormatTests(TestCase):
    def test_form_accepts_dd_mm_yyyy_input(self):
        form = TaskForm(data={
            'name': 'Тестове завдання',
            'description': 'Опис',
            'status': 'new',
            'priority': 1,
            'progress_termin': '31/12/2026',
        })

        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(str(form.cleaned_data['progress_termin']), '2026-12-31')
