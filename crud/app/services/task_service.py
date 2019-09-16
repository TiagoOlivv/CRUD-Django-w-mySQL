from ..models import tasks

def createTask(task):
    tasks.objects.create(name=task.name, about=task.about, date=task.date, priority=task.priority)

def listTask():
    return tasks.objects.all()