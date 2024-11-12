from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def message(request):
    return render(request,'Alert.html')

def success(request):
    messages.success(request,'Your Process is Success')
    return render(request,'Alert.html')


def info(request):
    messages.info(request,'Information Button Works')
    return render(request,'Alert.html')

def error(request):
    messages.error(request,'Error!!! Try again')
    return render(request,'Alert.html')

def warning(request):
    messages.warning(request,'Warning!!!')
    return render(request,'Alert.html')
