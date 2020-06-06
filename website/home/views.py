from django.shortcuts import render

from django.shortcuts import render,HttpResponse

def home(request):
    return render(request, 'home.html')
