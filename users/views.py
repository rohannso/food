from django.shortcuts import render,redirect
from .forms import *
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from  django.contrib.auth.decorators import login_required
def register_user(request):
    if request.method=='POST':
        form=Registerform(request.POST)
        if form.is_valid():
            form.save()
            
            username=form.cleaned_data.get('username')
            print(username)
            messages.success(request,f"welcome{username}")
            return redirect('users:login')
    else:
        form=Registerform ()
    return render(request,'users/useruser.html',{'form':form})  
from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('users:login')

@login_required
def profile(request):
    return render(request,'users/profile.html') 