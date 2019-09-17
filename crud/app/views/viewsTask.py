from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse
from ..entidades.task import task
from ..forms import taskform
from ..services import task_service


@login_required()
def home(request):
    tasks = task_service.listTask(request.user)
    return render(request, 'user/home.html', {'tasks': tasks})


@login_required()
def createTask(request):
    if request.method == 'POST':
        form_home = taskform(request.POST)
        if form_home.is_valid():
            name = form_home.cleaned_data["name"]
            about = form_home.cleaned_data["about"]
            date = form_home.cleaned_data["date"]
            priority = form_home.cleaned_data["priority"]
            newTask = task(name=name, about=about, date=date,
                           priority=priority, user=request.user)
            task_service.createTask(newTask)
            return redirect('home')
    else:
        form_home = taskform()
    return render(request, 'user/form_home.html', {'form_home': form_home})


@login_required()
def updateTask(request, id):
    taskDB = task_service.listTaskID(id)
    if taskDB.user != request.user:
        return HttpResponse("Não permitido")
    form_home = taskform(request.POST or None, instance=taskDB)
    if form_home.is_valid():
        name = form_home.cleaned_data["name"]
        about = form_home.cleaned_data["about"]
        date = form_home.cleaned_data["date"]
        priority = form_home.cleaned_data["priority"]
        newTask = task(name=name, about=about, date=date,
                       priority=priority, user=request.user)
        task_service.updateTask(taskDB, newTask)
        return redirect('home')
    return render(request, 'user/form_home.html', {'form_home': form_home})


@login_required()
def removeTask(request, id):
    taskDB = task_service.listTaskID(id)
    if request.method == 'POST':
        task_service.removeTask(taskDB)
        return redirect('home')
    return render(request, 'user/deleteTask.html', {'task': taskDB})
