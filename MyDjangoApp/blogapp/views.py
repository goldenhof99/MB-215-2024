from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("This is my first url")

def secondURL(request):
    return HttpResponse("This is my SECOND url")

def device(request, device_id):
    return render(request, 'blogapp/index.html', {'device_id': device_id})


