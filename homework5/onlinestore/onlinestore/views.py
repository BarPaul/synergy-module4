from django.shortcuts import render
from .constants import *

def menu(request):
    return render(request, 'index.html')

def samsung(request):
    return render(request, 'pattern.html', {'columns': COLUMNS, 'rows': SAMSUNG['rows'], 'name': 'Samsung'})

def iphone(request):
    return render(request, 'pattern.html', {'columns': COLUMNS, 'rows': IPHONE['rows'], 'name': 'Iphone'})

def xiaomi(request):
    return render(request, 'pattern.html', {'columns': COLUMNS, 'rows': XIAOMI['rows'], 'name': 'Xiaomi'})