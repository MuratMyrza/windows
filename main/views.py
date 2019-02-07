from django.http import HttpResponse
from django.shortcuts import render



def index(request):

    fruits = ['Apple', 'Banana', 'Cherry']

    return render(request, 'main/index.html', {
        'fruits': fruits,
    })

def something(request):
    return render(request, 'main/something.html')