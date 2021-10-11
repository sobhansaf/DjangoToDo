from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ToDoForm
from .models import Todo

class index(View):
    def get(self, request):
        return render(request, 'index.html', {'user': request.user})

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