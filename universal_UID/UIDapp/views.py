from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')



def loginpage(request):
    
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')   


