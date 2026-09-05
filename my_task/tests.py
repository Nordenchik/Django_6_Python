from django.test import TestCase

from .forms import TaskForm


class TaskFormDateFormatTests(TestCase):
    def test_form_accepts_dd_mm_yyyy_input(self):
        form = TaskForm(data={
            'name': 'Тестове завдання',
            'description': 'Опис',
            'status': 'todo',
            'priority': 1,
            'progress_termin': '31/12/2026',
        })

        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(str(form.cleaned_data['progress_termin']), '2026-12-31')

    def test_status_field_only_allows_three_ukrainian_choices(self):
        form = TaskForm(data={
            'name': 'Тестове завдання',
            'description': 'Опис',
            'status': 'todo',
            'priority': 1,
        })

        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.fields['status'].choices, [
            ('todo', 'Потрібно зробити'),
            ('in_progress', 'У процесі'),
            ('done', 'Готово'),
        ])

        invalid_form = TaskForm(data={
            'name': 'Тестове завдання',
            'description': 'Опис',
            'status': 'blocked',
            'priority': 1,
        })

        self.assertFalse(invalid_form.is_valid())
        self.assertIn('status', invalid_form.errors)
