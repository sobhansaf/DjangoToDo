from django.views import View
from django.shortcuts import render

class index(View):
    def get(self, request):
        return render(request, 'index.html', {'user': request.user})