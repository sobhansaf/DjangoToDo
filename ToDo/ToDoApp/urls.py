from django.urls import *

from .views import index

urlpatterns = [
    path('', index.as_view(), name='index'),
]