from django.shortcuts import render, redirect
from .models import Todolists
from django.views import View
from django.contrib import messages
from datetime import date


# Create your views here.

# class home(View):
#     def get(self, request):
#         todo = Todolists.objects.all()
#         return render(request, 'index.html', {'tasks': todo})


# class add(View):
#     def get(self, request):
#         return render(request, 'add-todo.html')

#     def post(self, request):
#         if request.method == 'POST':
#             title = request.POST.get("taskName")
#             description = request.POST.get("taskDescription")
#             due = request.POST.get("taskDue")
#             todo = Todolists()
#             todo.title = title
#             todo.description = description
#             todo.due = due
#             if title == '' or due == '':
#                 if title == '' and due == '':
#                     messages.info(
#                         request, 'Title and Due Date should not be empty ')
#                 elif title == '':
#                     messages.info(request, 'Title should not be empty')
#                 elif due == '':
#                     messages.info(request, 'Due Date should not be empty')
#                 return redirect("/todo")
#             else:
#                 todo.save()
#                 return redirect("/")


# class delete(View):
#     def get(self, request, id):
#         todo = Todolists.objects.get(id=id)
#         todo.delete()
#         return redirect("/")


# class update(View):
#     def get(self, request, id):
#         todo = Todolists.objects.get(id=id)
#         print(todo.due)
#         return render(request, 'update-todo.html', {'tasks': todo})

#     def post(self, request, id):
#         todo = Todolists.objects.get(id=id)
#         title = request.POST.get("taskName")
#         description = request.POST.get("taskDescription")
#         due = request.POST.get("taskDue")
#         button = request.POST.get("ButtonPressed")
#         print(button)
#         status = request.POST.get("taskStatus")
#         todo.title = title
#         todo.description = description
#         todo.due = due
#         todo.status = status
#         todo.save()
#         return redirect("/")


# class view(View):
#     def get(self, request, id):
#         todo = Todolists.objects.get(id=id)
#         print(todo.due)
#         return render(request, 'view.html', {'tasks': todo})



class TodoView():
    def home(self,request):
        todo = Todolists.objects.all()
        return render(request, 'index.html', {'tasks': todo})


    def delete(self,request, id):
        todo = Todolists.objects.get(id=id)
        todo.delete()
        return redirect("/")


    def add(self,request):
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
        return render(request, 'add-todo.html')
    
    def view(self,request, id):
        todo = Todolists.objects.get(id=id)
        print(todo.due)
        return render(request, 'view.html', {'tasks': todo})


    def update(self,request, id):
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
        else:
            todo = Todolists.objects.get(id=id)
            print(todo.due)
            return render(request, 'update-todo.html', {'tasks': todo})