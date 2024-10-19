from django.shortcuts import render , redirect
from UIDapp.models import *
from django.contrib import messages

# from django.contrib .auth import authenticate
# Create your views here.

def home(request):
    return render(request, 'home.html')

def loginpage(request):
    if request.method == "POST":
        uid = request.POST.get("uid")
        password = request.POST.get("password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        try:
            user = UIDmodel.objects.get(UID=uid)
                 # Check if the current password is correct
            if user.password != password:
                messages.error(request, "Current password is incorrect.")
                return render(request, 'login.html')

            # Check if new password and confirmation match
            if new_password != confirm_password:
                messages.error(request, "New passwords do not match.")
                return render(request, 'login.html')

            # Update the password
            user.password = new_password
            user.save()
            messages.success(request, "Password updated successfully.")
            return redirect('/home')  # Redirect to home page after successful update
        except UIDmodel.DoesNotExist:
            messages.error(request, "User with this UID does not exist.")
        

    
    return render(request, 'login.html')


def signup(request):
    context={}
    
    if request.method == "POST" :
        username = request.POST.get("username")
        phno=request.POST.get("phone")
        email = request.POST.get("email")
        
        
        uID=UIDmodel.objects.create(username = username, phno = phno, email = email)
        uID.save()

        Database =UIDmodel.objects.values('username','UID','password')
        New_user = Database[len(Database)-1]  # we use len() to findout lastest user detailsand although we can't use -ve slicing

        context={ 
            'username':New_user.get('username','not found'),
            'UID': New_user.get('UID', 'No UID Found'),
            'password': New_user.get('password', 'No Password Found'),
        }

        return render(request, 'signup.html',context)

        
    return render(request, 'signup.html',context)   
    # messages.info(request,"account created.")

        


