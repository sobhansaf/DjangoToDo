from django.urls import path

from .views import ToDoList, index, Change_todo_status

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('new/', ToDoList.as_view(), name='new_todo'),
    path('change/<int:todo_id>/', Change_todo_status.as_view(), name='change_todo_status')
]