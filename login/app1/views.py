from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):

            if request.method=='POST':
                username=request.POST['username']
                password=request.POST['password']

                x=User.objects.create_user(username=username,password=password)
                x.save()
                print('user created')
                return redirect('home')
            else:
                return render(request,"a.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        from django.contrib import auth
        x=auth.authenticate(username=username,password=password)
        if x is None:
            return HttpResponse("<h2>Please enter the correct cerdentials</h2>")
        else:
            return render(request,'wc.html')
    else:
        return render(request, "b.html")

def wc(request):
    return render(request,'wc.html')
