from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, "twitter/register.html", {'form': forms.userRegister})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            # register user
            try:
                user = User.objects.create_user(
                    first_name=request.POST["first_name"],
                    username=request.POST["username"],
                    email=request.POST["email"],
                    password=request.POST["password1"])
                user.save()

                #login(request, user)

                return redirect("home")
            except IntegrityError:
                return render(request, "twitter/register.html", {'form': forms.userRegister, "error": "User already exist "})
        else:
            return render(request, "twitter/register.html", {'form': forms.userRegister, "error": "Password do not match"})

   

def login_session(request):
        if request.method == "GET":
            return render(request, "twitter/login.html", {"form": AuthenticationForm})
        else:
            user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "twitter/login.html", {"form": AuthenticationForm,
                                                  "error": "Username o password is incorrect"})
        else:
            login(request, user)
            return redirect("home")

def logout_session(request):
    logout(request)
    return redirect("login")