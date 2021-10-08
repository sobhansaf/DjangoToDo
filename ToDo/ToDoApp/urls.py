from django.urls import path

from .views import index, SignUp, SignIn

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', SignIn.as_view(), name='login'),
    path('', index.as_view(), name='index'),
]
