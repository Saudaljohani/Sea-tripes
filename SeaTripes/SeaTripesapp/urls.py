from django.urls import path
from . import views

app_name = "SeaTripesapp"

urlpatterns = [

    path('', views.home_page, name="home_page"),
    path('about/',views.toviwe, name ="about_us"),

]