from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'Потрібно зробити'),
        ('in_progress', 'У процесі'),
        ('done', 'Готово'),
    ]

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    priority = models.IntegerField()
    progress_termin = models.DateField(null=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.name
