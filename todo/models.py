from django.db import models
from datetime import date

class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False,null=False, verbose_name='Título')
    description = models.TextField(blank=True,null=True, verbose_name='Descripción')
    date = models.DateField(default=date.today, verbose_name='Fecha creación')
    estimated_end = models.DateField(blank=True, null= True, verbose_name='Fecha de finalización')
    priority = models.IntegerField(default=3, verbose_name='Prioridad')

    def __str__(self):
        return self.title
