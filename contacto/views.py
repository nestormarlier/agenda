from django.shortcuts import render,redirect
from .models import Contacto
from .forms import ContactoForm
from django.contrib import messages

def index(request):
    contactos = Contacto.objects.filter(name__contains=request.GET.get('search', ''))
    return render(request, 'contact/index.html',{'contactos': contactos})

def view(request, id):
    contact = Contacto.objects.get(id=id)
    return render(request, 'contact/detail.html', {'contact': contact})

def edit(request, id):
    contact = Contacto.objects.get(id=id)
    if request.method == 'GET':
        form = ContactoForm(instance=contact)
        return render(request, 'contact/edit.html', {'form': form, 'contact': contact})
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance = contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contacto actualizado')
        return render(request, 'contact/edit.html',{'form': form, 'contact': contact})

def create(request):
    if request.method == 'GET':
        form = ContactoForm()
        return render(request, 'contact/create.html', {'form': form})
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')

def delete(request,id):
        contact = Contacto.objects.get(id=id)
        contact.delete()
        return redirect('contact')