from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()

def user_register(request): 
    if request.method =='POST':
        new_user = User(
            email= request.POST['email'],
            username=request.POST['username']
        )
        new_user.set_password(request.POST['password'])
        new_user.save()
        login(request, new_user)
        return redirect('missing_persons:home')
        #return redirect('accounts:login')
       # return render(request, 'accounts/login.html')
    return render(request, 'accounts/register.html')

def user_login(request): 
    if request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            login(request, user)
            print(user.id)
            print(user.username)
            return redirect('missing_persons:home')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')