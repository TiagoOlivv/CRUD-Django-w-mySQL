from django.shortcuts import render
from .forms import taskform

def home(request):
    var = 'teste'
    return render(request, 'user/home.html', {'var' : var})

def createTask(request):
    form_home = taskform()
    return render(request, 'user/form_home.html', {'form_home' : form_home})