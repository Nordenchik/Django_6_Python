from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, help_text='Опишіть завдання.', null=True, blank=True)
    image = models.ImageField(upload_to='images/', help_text='Вставте зображення для завдання.', null=True, blank=True)
    status = models.CharField(max_length=100)
    priority = models.IntegerField()
    progress_termin = models.DateField(help_text='Вкажіть термін виконання завдання. (YYYY-MM-DD)', null=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.name
