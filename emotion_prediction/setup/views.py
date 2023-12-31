from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,views as auth_views

def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            return HttpResponse("Passwords do not match")

        # Create a new user
        my_user = User.objects.create_user(username=username,email=email, password=password, first_name=first_name, last_name=last_name)
        
        return HttpResponse("User created successfully")
  
    return render(request, 'sign_up.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(paragraph)
        else:
             return redirect(user_login_error)

    return render(request, 'logiin.html')


def user_login_error(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(paragraph)
        else:
            return redirect(user_login_error)

    return render(request, 'login_error.html')



from django.contrib.auth.forms import PasswordResetForm


































def paragraph(request):
    return render(request, 'emoji.html')

def whole(request):
    return render(request, 'emoji-whole.html')

def profile(request):
    user = request.user  # Replace this with your user retrieval logic

    context = {
        'user': user,
    }
    return render(request, 'profile.html')

def change(request):
    if request.method== 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

    
    return render(request,'changepass.html')