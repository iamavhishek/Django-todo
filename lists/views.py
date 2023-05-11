from django.shortcuts import render, redirect
from .models import Todolists
from django.http import HttpResponse

tasks = [
    {'id': 1, 'name': 'Finish your proposal',
     'description': 'Finish and Print the Project II proposal and submit it to sameer sir', 'status': 'awaiting'},
    {'id': 2, 'name': 'Go to market',
     'description': 'Go to market to buy some vegetables and fruits', 'status': 'completed'},
    {'id': 3, 'name': 'Learn Django',
     'description': 'Go to office and continue learning django', 'status': 'inprocess'},
    {'id': 4, 'name': 'Sleep at 10',
     'description': 'Go to bed at 10PM sharp', 'status': 'completed'},
]


# Create your views here.


def home(request):
    todo = Todolists.objects.all()
    return render(request, 'lists/index.html', {'tasks': todo})


def delete(request, id):
    todo = Todolists.objects.get(id=id)
    todo.delete()
    return redirect("/")


def add(request):
    if request.method == 'POST':
        title = request.POST.get("taskName")
        description = request.POST.get("taskDescription")
        due = request.POST.get("taskDue")
        todo = Todolists()
        todo.title = title
        todo.description = description
        todo.due = due
        todo.save()
        return redirect("/")
    return render(request, 'lists/add-todo.html')


def update(request, id):
    todo = Todolists.objects.get(id=id)
    print(todo.due)
    return render(request, 'lists/update-todo.html', {'tasks': todo})


def update_it(request, id):
    if request.method == 'POST':
        todo = Todolists.objects.get(id=id)
        title = request.POST.get("taskName")
        description = request.POST.get("taskDescription")
        due = request.POST.get("taskDue")
        status = request.POST.get("taskStatus")
        todo.title = title
        todo.description = description
        todo.due = due
        todo.status = status
        todo.save()
        return redirect("/")
