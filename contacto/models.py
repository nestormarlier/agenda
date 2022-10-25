from logging import PlaceHolder
from multiprocessing import Value
from operator import mod
from unicodedata import name
from django.db import models
from datetime import date

class Contacto(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=40, blank=False, null=False)
    tel_uno = models.CharField(max_length=10)
    tel_dos = models.CharField(max_length=10)
    email = models.EmailField(max_length=60, blank=False, null=False)
    company = models.CharField(max_length=100, blank=False, null=False)
    date_create = models.DateField(default = date.today)

    def __str__(self):
        return self.name