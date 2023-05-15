from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.TodoView().home, name='home'),
#     path('todo/', views.TodoView().add, name='add'),
#     path('todo/<int:id>/delete', views.TodoView().delete, name='delete'),
#     path('todo/<int:id>/edit', views.TodoView().edit, name='update'),
#     path('todo/<int:id>/view', views.TodoView().view, name='view')
# ]

urlpatterns = [
    path('', views.TodoView().home, name='home'),
    path('todo/', views.TodoView().add, name='add'),
    path('todo/<int:id>/delete', views.TodoView().delete, name='delete'),
    path('todo/<int:id>/edit', views.TodoView().update, name='update'),
    path('todo/<int:id>/view', views.TodoView().view, name='view')
]