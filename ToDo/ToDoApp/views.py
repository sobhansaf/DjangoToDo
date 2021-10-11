from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ToDoForm
from .models import Todo

class index(View):
    def get(self, request):
        todo_list = []
        all = request.GET.get('all', 0)   # if all is 1 then done and undone tasks will be shown
        try:
            all = int(all)
        except:
            all = 0
        if request.user.is_authenticated:
            if all != 1:
                todo_list = Todo.objects.filter(user=request.user, done=False).order_by('date')
            else:
                todo_list = Todo.objects.filter(user=request.user).order_by('date')
        return render(request, 'index.html', {'user': request.user, 'todo_list': todo_list, 'all': all})

class ToDoList(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    
    def get(self, request):
        form = ToDoForm()
        if request.session.get('data', False) or ('data' in request.session and len(request.session['data']) == 0):
            form = ToDoForm(request.session['data'])
            form.is_valid()
            request.session.pop('data')

        return render(request, 'add-todo.html', {'form': form})

    def post(self, request):
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('index')
        
        self.request.session['data'] = request.POST
        return redirect('new_todo')


class Change_todo_status(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'

    def post(self, request, todo_id):
        try:
            todo = Todo.objects.get(user=request.user, id=todo_id)
            todo.done = not todo.done
            todo.save()
        except:
            pass
        return redirect('index')