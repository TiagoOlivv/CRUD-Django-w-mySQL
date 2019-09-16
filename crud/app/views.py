from django.shortcuts import render, redirect
from .forms import taskform
from .entidades.task import task
from .services import task_service

def home(request):
    tasks = task_service.listTask()
    return render(request, 'user/home.html', {'tasks' : tasks})

def createTask(request):
    if request.method == 'POST':
        form_home = taskform(request.POST)
        if form_home.is_valid():
            name = form_home.cleaned_data["name"]
            about = form_home.cleaned_data["about"]
            date = form_home.cleaned_data["date"]
            priority = form_home.cleaned_data["priority"]   
            newTask = task(name=name , about=about, date=date, priority=priority)
            task_service.createTask(newTask)
            return redirect('home')
    else:
        form_home = taskform()
    
    return render(request, 'user/form_home.html', {'form_home' : form_home})