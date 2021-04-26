from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Todo

def index(request):
    items = Todo.objects.order_by('-id')
    return render(request, 'todo/index.html', {'items': items})

def done(request):
    items = Todo.objects.filter(status=True).order_by('-id')
    return render(request, 'todo/index.html', {'items': items})

def pending(request):
    items = Todo.objects.filter(status=False).order_by('-id')
    return render(request, 'todo/index.html', {'items': items})

def delete_all(request):
    return render(request, 'todo/index.html')

def update(request, id):
    return render(request, 'todo/index.html')

def create(request):
    return render(request, 'todo/index.html')

def delete(request, id):
    return render(request, 'todo/index.html')