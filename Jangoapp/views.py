from django.shortcuts import render,redirect
from .forms import UserCreateForm,LoginForm,UserForm
from .models import User,UserLoginActivity
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'About.html')

def SignUp(request):
    if request.method=='POST':
        form=UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreateForm()
    return render(request,'registration/signup.html',{'form':form})

def login(request):
    """ USer login view """
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid:
            login(request,form)
            return redirect('home')
    else:
        form=LoginForm()
        return render(request,'registration/login.html',{'form':form})
@login_required
def list(request):
    """ List of activity periods """
    text={'list': UserLoginActivity.objects.all()}
    return render(request,'member_list.html',text)

@login_required
def delete(request,id):
    """ User activity periods deleting """
    member=UserLoginActivity.objects.get(pk=id)
    member.delete()
    return redirect('list')

