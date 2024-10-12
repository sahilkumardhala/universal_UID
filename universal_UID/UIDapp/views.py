from django.shortcuts import render,HttpResponse
import random
from UIDapp.models import *
# from django.db import models
# Create your views here.

def home(request):
    return render(request, 'home.html')

def loginpage(request):
    
    return render(request, 'login.html')

def unique_user_UID():
            prefix = "UID"
            while True:
                random_number = random.randint(1000, 9999)  # Generate a random number of 4 digits
                UID = f"{prefix}{random_number}"
                if not UIDmodel.objects.filter(UID=UID).exists():
                    return UID

def signup(request):
    if request.method == "POST" :
        username = request.POST.get("username")
        phno=request.POST.get("phone")
        email = request.POST.get("email")

        
        
    
        

        








    return render(request, 'signup.html')   


