from django.urls import path
from . import views

app_name = "SeaTripesapp"

urlpatterns = [

    path('', views.home_page, name="home_page"),
    path('about/',views.about_us, name ="about_us"),
    path('Choose/marina/',views.Choose_marina, name = "marina_page"),
    path('contact/',views.contact,name = "contact"),
    path("add/Captain/",views.add_Captain, name="add_Captain"),
    path("list/Captains/",views.list_Captains, name="list_Captains"),
    
    path("add/trip/",views.add_trip,name="add_trip"),
    path("list/trip/",views.list_trip,name="list_trip")
   
    
]