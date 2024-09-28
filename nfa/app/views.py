

from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def teacher(request):
    return render(request, 'teacher.html')

def vehicle(request):
    return render(request, 'vehicle.html')

def contact(request):
    return render(request, 'contact.html')




