from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.

# def home(request):
    
#     return render(request,'home.html')

def signup_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    context={}
    if request.method == 'POST':
        un = request.POST.get('un','')
        email = request.POST.get('em','')
        pw1 = request.POST.get('psw','')
        pw2 = request.POST.get('cpsw','')
        if pw1 == pw2:
            if User.objects.filter(username=un):
                context['error']='Username Already Exits'
            else:
                User.objects.create_user(
                    username=un,
                    email=email,
                    password=pw1,
                )
                return redirect('login') 
        else:
            context['error'] = 'Password does not match '
            
    return render(request,'signup.html',context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    context={}
    if request.method == 'POST':
        un = request.POST.get('un','')
        pw = request.POST.get('psw','')

        user = authenticate(request,username = un, password = pw) 

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            context['error'] = 'Invalid credentials'
            return redirect('signup')

    return render(request,'login.html',context)

def logout_user(request):
    logout(request)
    return redirect('login')