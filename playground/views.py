from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Request handler

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    # pull data from db
    # transform data
    # send email
    # return HttpResponse('Hello')
    x = calculate()
    return render(request, 'index.html', {'name': 'Kristina'}                   )
