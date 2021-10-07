from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login

from .forms import SignupForm

class index(View):
    def get(self, request):
        return render(request, 'index.html', {'user': request.user})

class SignUp(View):
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('index')
        return render(request, 'signup.html', {'signupform': form})

    def get(self, request):
        form = SignupForm()
        return render(request, 'signup.html', {'signupform': form})