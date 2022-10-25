from unicodedata import name
from django.urls import path

from contacto.views import delete, edit
from . import views

urlpatterns = [
    path('', views.index, name='todo'),
    path('view/<int:id>', views.view, name='todo_view'),
    path('edit/<int:id>', views.edit, name='todo_edit'),
    path('delete/<int:id>', views.delete, name='todo_delete'),
    path('create/', views.create, name="todo_create")
]