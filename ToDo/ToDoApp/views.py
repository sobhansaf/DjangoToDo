from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login

from .forms import SignupForm

class index(View):
    def get(self, request):
        return render(request, 'index.html', {'user': request.user})

class SignUp(View):
    def post(self, request):
        # response to a post request is redirect
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('index')
        
        # saving data in session, in order to show errors after redirection
        request.session['wrong'] = True
        request.session['data'] = request.POST
        return redirect('signup')        

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        form = SignupForm()
        if request.session.get('wrong', False):
            # if the request was the result of a redirect after a post request with wrong data
            form = SignupForm(request.session.get('data'))
            request.session.pop('data')
            request.session.pop('wrong')
            form.is_valid()
        return render(request, 'signup.html', {'signupform': form})
