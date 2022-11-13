from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page(request:HttpRequest):

    return render(request,"SeaTripesapp/home.html")

def toviwe(request:HttpRequest):

    return render(request,"SeaTripesapp/toviwe.html")