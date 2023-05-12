from django.shortcuts import render, redirect
from .models import Todolists
from django.views import View

# tasks = [
#     {'id': 1, 'name': 'Finish your proposal',
#      'description': 'Finish and Print the Project II proposal and submit it to sameer sir', 'status': 'awaiting'},
#     {'id': 2, 'name': 'Go to market',
#      'description': 'Go to market to buy some vegetables and fruits', 'status': 'completed'},
#     {'id': 3, 'name': 'Learn Django',
#      'description': 'Go to office and continue learning django', 'status': 'inprocess'},
#     {'id': 4, 'name': 'Sleep at 10',
#      'description': 'Go to bed at 10PM sharp', 'status': 'completed'},
# ]


# Create your views here.

class home(View):
    def get(self, request):
        todo = Todolists.objects.all()
        return render(request, 'index.html', {'tasks': todo})


class add(View):
    def get(self, request):
        return render(request, 'add-todo.html')

    def post(self, request):
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


class delete(View):
    def get(self, request, id):
        todo = Todolists.objects.get(id=id)
        todo.delete()
        return redirect("/")


class update(View):
    def get(self, request, id):
        todo = Todolists.objects.get(id=id)
        print(todo.due)
        return render(request, 'update-todo.html', {'tasks': todo})

    def post(self, request, id):
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


class view(View):
    def get(self, request, id):
        todo = Todolists.objects.get(id=id)
        print(todo.due)
        return render(request, 'view.html', {'tasks': todo})
