from operator import imod
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')