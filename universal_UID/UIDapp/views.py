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
    user={}
    uids={}
    pws={}
    if request.method == "POST" :
        username = request.POST.get("username")
        phno=request.POST.get("phone")
        email = request.POST.get("email")
        
        
        uID=UIDmodel.objects.create(username = username, phno = phno, email = email)

        uID.save()
        #Database =UIDmodel.objects.all()
        Database_ =UIDmodel.objects.values('username','UID','password')
        data = Database_[len(Database_)-1]
        recent_user= UIDmodel.objects.latest('UID')
        context={ 
            'username':data.get('username','not found'),
            'UID': data.get('UID', 'No UID Found'),
            'password': data.get('password', 'No Password Found'),
        }
        return render(request, 'signup.html',context) 
        
        

    return render(request, 'signup.html',context)   



    # messages.info(request,"account created.")
        


