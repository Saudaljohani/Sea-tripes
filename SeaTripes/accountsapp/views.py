from django.http import HttpRequest, HttpResponse
from django.shortcuts import render ,redirect
# Create your views here.

#for login user
def login(request:HttpRequest):

    return render(request,"accountsapp/login.html")

# for registion user
def registion_user(request:HttpRequest):

    return render(request,"accountsapp/registration.html")

#for registion user as Captain
def registion_Captain(request:HttpRequest):

    return render(request,"accountsapp/Captain_Registration.html")
