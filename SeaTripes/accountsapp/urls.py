from django.urls import path
from . import views

app_name = "accountsapp"

urlpatterns = [
    path("login/",views.login,name ="login"),
    path("registration/",views.registion_user, name="registration"),
    path("Captain/Registration/",views.registion_Captain,name="Captain_Registr"),

]