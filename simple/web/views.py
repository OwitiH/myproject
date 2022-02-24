from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, "web\index.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass0 = request.POST.get('pass0')
        pass1 = request.POST.get('pass1')

        myuser = User.objects.create_user(username, email, pass0)
        myuser.first_name = fname
        myuser.last_name = lname


        myuser.save()

        messages.success(request, "your account has been successfully created")

        return redirect('signin')

    return render(request, "web\signup.html")


def signin(request):
    return render(request, "web\signin.html")


def signout(request):
    pass
