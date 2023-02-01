from django.shortcuts import render

# Create your views here.


def home(request):
    dom = 'Hello World'
    context = {
        'dom' : dom,
    }
    return render(request, 'main.html', context)


def home2(request):
    dom = 'Hello dom'
    context = {
        'dom' : dom,
    }
    return render(request, 'test.html', context)