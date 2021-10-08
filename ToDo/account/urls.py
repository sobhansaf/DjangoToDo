from django.urls import path

from .views import SignUp, SignIn, Logout

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', SignIn.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
