from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, '0114_django_demo.html', {})

