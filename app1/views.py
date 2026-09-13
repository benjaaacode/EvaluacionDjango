from django.shortcuts import render

def vista1(request):
    return render(request, 'app1/vista1.html')

def vista2(request):
    return render(request, 'app1/vista2.html')