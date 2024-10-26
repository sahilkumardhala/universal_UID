from django.shortcuts import render , redirect
from UIDapp.models import *
from django.contrib import messages
# from django.contrib .auth import login as auth_login
# from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'home.html')

def set_password(request):
        
    if request.method == "POST":
        uid = request.POST.get("uid")
        password = request.POST.get("password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        # default_password=UIDmodel.password.default()
        try:
            user = UIDmodel.objects.get(UID=uid)
                 # Check if the current password is correct
            if user.password != password:
                messages.error(request, "Current password is incorrect.")
                return render(request, 'set_password.html')

            # Check if new password and confirmation match
            if new_password != confirm_password:
                messages.error(request, "New passwords do not match.")
                return render(request, 'set_password.html')

            # Update the password
            user.password = new_password
            user.save()
            messages.success(request, "Password updated successfully.")
            return redirect('/')  # Redirect to home page after successful update
        except UIDmodel.DoesNotExist:
            messages.error(request, "User with this UID does not exist.")
        

    
    return render(request, 'set_password.html')


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



def login(request):
    if request.method == "POST":
        uid = request.POST.get("uid")
        password = request.POST.get("password")

        try:
            user = UIDmodel.objects.get(UID=uid)
            if user.password == password:
                # Set session to keep the user logged in
                request.session['user_id'] = user.id
                messages.success(request, "Login successful.")
                return redirect('/User_dashboard')  # Redirect to the user dashboard
            else:
                messages.error(request, "Incorrect password.")
        except UIDmodel.DoesNotExist:
            messages.error(request, "User with this UID does not exist.")

    return render(request, 'login.html')


def custom_login_required(function):
    def wrap(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('/login')  # Redirect to login if not logged in
        return function(request, *args, **kwargs)
    return wrap




@custom_login_required
def User_dashboard(request):
       
        return render(request, 'user_dashboard.html')


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    messages.success(request, "Logged out successfully.")
    return redirect('/login')

