from django.shortcuts import render
from UIDapp.models import *
from django.contrib import messages

# from django.contrib .auth import authenticate
# Create your views here.

def home(request):
    return render(request, 'home.html')

def loginpage(request):
    
    return render(request, 'login.html')


def signup(request):
    context={}
    if request.method == "POST" :
        username = request.POST.get("username")
        phno=request.POST.get("phone")
        email = request.POST.get("email")

        
        uID=UIDmodel.objects.create(username = username, phno = phno, email = email)
        uID.save()
        Database =UIDmodel.objects.all()
        context={ "UIDdatas" : Database }

    # messages.info(request,"account created.")

    return render(request, 'signup.html',context)   


