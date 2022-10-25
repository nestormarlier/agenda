from django.forms import ModelForm
from .models import Contacto

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        #fields = ('name', 'last_name', 'tel_uno', 'tel_dos','email', 'company',)
        #fields = '__all__'
        exclude = ('date_create',)