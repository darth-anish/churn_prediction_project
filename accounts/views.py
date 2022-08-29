from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            return redirect('prediction:home')
        else:
            messages.error(request, "Email/Password wrong, Please try again!")
    
    return render(request, 'registration/login.html')

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
