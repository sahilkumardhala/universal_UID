from django.shortcuts import render,HttpResponse

# Create your views here.

def loginpage(request):
    return HttpResponse("hii")
    #return render(request, 'login.html')