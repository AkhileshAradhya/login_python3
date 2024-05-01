from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name="home"),
   path('ulogin',views.ulogin,name="ulogin"),
   path('signin',views.signin,name="signin"),
   path('signout',views.signout,name="signout"),
   path('index',views.index,name="index"),
]
