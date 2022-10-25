from django.contrib import messages
from django.shortcuts import render, redirect

import todo
from .models import Todo
from .forms import TodoForm

def index(request):
    tareas = Todo.objects.filter(title__contains=request.GET.get('search', ''))
    return render(request, 'todo/index.html', {'tareas': tareas})

def view(request, id):
    tarea = Todo.objects.get(id=id)
    return render(request, 'todo/detail.html', {'tarea': tarea})

def edit(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/edit.html', {'form': form, 'tarea': todo})
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contacto actualizado')
            return render(request, 'todo/edit.html', {'form':form, 'tarea': todo})

def delete(request, id):
    tarea = Todo.objects.get(id=id)
    tarea.delete()
    return redirect('todo')

def create(request):
    if request.method == 'GET':
        form = TodoForm()
        return render(request, 'todo/create.html', {'form': form})
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')