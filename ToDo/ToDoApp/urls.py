from django.urls import path

from .views import ToDoList, index

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('new/', ToDoList.as_view(), name='new_todo')
]