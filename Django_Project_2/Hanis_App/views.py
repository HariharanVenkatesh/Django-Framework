from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'Project.html')

def Register(request):
    Name = request.POST['Name']
    Password = request.POST['Password']
    Address = request.POST['Address']
    Email = request.POST['Email']
    return render(request,"AppResult.html",{'Name':Name, 'Password':Password, 'Address':Address, 'Email':Email})