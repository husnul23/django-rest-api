from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'todo/index.html')

def done(request):
    return render(request, 'todo/index.html')

def pending(request):
    return render(request, 'todo/index.html')

def delete_all(request):
    return render(request, 'todo/index.html')

def update(request):
    return render(request, 'todo/index.html')

def create(request):
    return render(request, 'todo/index.html')

def delete(request):
    return render(request, 'todo/index.html')