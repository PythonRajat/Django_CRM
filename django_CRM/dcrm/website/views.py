from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
# Create your views here.
def home(request):
    records = Record.objects.all()
    # check to see if logging In
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=uname,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have logged in successfully")
            return redirect('home')
        else:
            messages.success(request, "error login again")
   
    return render(request,'index.html',{'records':records})


def logout_user(request):
    logout(request)

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully registered!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})