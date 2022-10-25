from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contacto.urls')),
    path('todo/', include('todo.urls')),
    path('', views.index, name='index')
]
