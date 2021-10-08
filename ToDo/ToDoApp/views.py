from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignupForm, SignInForm

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

class SignIn(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        
        # if the request was the result of a redirect from post request with wrong credentials, wrong var would be true
        # this results in showing an error which says "credentials were wrong" in login page 
        wrong = False
        if request.session.get('wrong_credentials', False):
            wrong = True
            request.session.pop('wrong_credentials')
        form = SignInForm()
        return render(request, 'login.html', {'form': form, 'wrong': wrong })

    def post(self, request):
        # post requests are responded with a redirect
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect('index')
        request.session['wrong_credentials'] = True   # with wrong credentials when going back to login page, it should show an error
        return redirect('login')