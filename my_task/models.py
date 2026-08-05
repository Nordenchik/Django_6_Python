from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, help_text='Опишіть завдання...')
    status = models.CharField(max_length=100)
    priority = models.IntegerField()
    progress_termin = models.DateField()
