from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('todo/', views.add.as_view(), name='add'),
    path('todo/<int:id>/delete', views.delete.as_view(), name='delete'),
    # path('todo/update/<int:id>', views.update, name='update'),
    path('todo/<int:id>', views.update.as_view(), name='update'),
    path('todo/<int:id>/view', views.view.as_view(), name='view')
]
