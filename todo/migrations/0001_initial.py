# Generated by Django 4.1 on 2022-10-16 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Fecha creación')),
                ('estimated_end', models.DateField(blank=True, null=True, verbose_name='Fecha de finalización')),
                ('priority', models.IntegerField(default=3, verbose_name='Prioridad')),
            ],
        ),
    ]
