from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .models import Captain , Trip

# Create your views here.


def home_page(request:HttpRequest):

    return render(request,"SeaTripesapp/home.html")
#ro viwe about_us
def about_us(request:HttpRequest):

    return render(request,"SeaTripesapp/about_us.html")
#to start location of the trip
def Choose_marina(request:HttpRequest):

    return render(request,"SeaTripesapp/Choose_marina.html")

def contact(request:HttpRequest):

    return render(request,"SeaTripesapp/contact.html")


#to add Captain
def add_Captain(request : HttpRequest):

    if request.method == "POST":
        new_Captain = Captain(name_Captain=request.POST["name_Captain"], age_Captain = request.POST["age_Captain"], dec_Captain=request.POST["dec_Captain"])
        new_Captain.save()


    return render(request, "SeaTripesapp/add_Captain.html")

##add trip 
def add_trip(request : HttpRequest):
    if request.method == "POST":
        new_trip=Trip(titile=request.POST["titile"],dec=request.POST["dec"],date=request.POST["date"],pic=request.FILES["pic"])
        new_trip.save()
    return render(request, "SeaTripesapp/add_trip.html")

def list_trip(request : HttpRequest):
    
    trips = Trip.objects.all()

    return render(request, "SeaTripesapp/list_trip.html", {"trips" : trips})


#all#
def list_Captains(request: HttpRequest):
    
    
    if "search" in request.GET:
        Captains = Captain.objects.filter(title__contains=request.GET["search"])
    else:
        Captains = Captain.objects.all()

    
    return render(request, "SeaTripesapp/list_Captains.html", {"Captains" : Captains})