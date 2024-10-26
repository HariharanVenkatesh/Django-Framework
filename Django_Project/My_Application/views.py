from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request,'home.html')

def Product(request):
    Mobile = int(request.GET["Mobile"])
    Keyboard = int(request.GET["Keyboard"])
    Monitor = int(request.GET["Monitor"])
    price = Mobile+Keyboard+Monitor
    return render(request,'Result.html',{'Price':price})