from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,'new.html')

def second(request):
    return render(request,'new2.html')

def third(request):
    return render(request,'new3.html')

def last(request):
    return render(request,'new4.html')
