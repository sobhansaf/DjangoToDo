from django.urls import path

from .views import index, SignUp

urlpatterns = [
    path('signup/', SignUp.as_view()),
    path('', index.as_view(), name='index'),
]
