from django.shortcuts import redirect, render
from django.http import HttpResponse
from.models import Info
# Create your views here.
def home(request): # 127.0.0.1:8000/
    myinfo = Info.objects.all()
    if(myinfo!=''):
        return render(request, "Admin.html",{'info':myinfo})
    else:    
        return render(request, "Admin.html")

    

def addinfo(request): # 127.0.0.1:8000/addinfo
     if request.method=='POST':
        name = request.POST['name']
        age = request.POST['age']
        qualification = request.POST['qualification']
        address = request.POST['address']
        phoneno = request.POST['phoneno']
        email = request.POST['email']

        obj = Info()
        obj.Name = name
        obj.Age = age
        obj.Qualification = qualification
        obj.Address = address
        obj.PhoneNo = phoneno
        obj.Email = email
        obj.save()
        myinfo = Info.objects.all()
        return redirect('home')
     return render(request, "Admin.html")

def updateinfo(request,id): # 127.0.0.1:8000/updateinfo
    myinfo=Info.objects.get(id=id)
    if request.method=="POST":
        name = request.POST['name']
        age = request.POST['age']
        qualification = request.POST['qualification']
        address = request.POST['address']
        phoneno = request.POST['phoneno']
        email = request.POST['email']

        myinfo.Name=name
        myinfo.Age=age
        myinfo.Qualification=qualification
        myinfo.Address=address
        myinfo.PhoneNo=phoneno
        myinfo.Email=email
        myinfo.save()
        return redirect('home')
    return render(request,'Update.html',{'data':myinfo})


def deleteinfo(request,id): # 127.0.0.1:8000/deleteinfo/id
     myinfo=Info.objects.get(id=id)
     myinfo.delete()
     return redirect('home')


