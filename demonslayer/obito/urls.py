from django.contrib import admin

from django.urls import path
from . import views

urlpatterns = [
path("",views.home,name="home"),
path("about",views.about,name="about"),
path("contact",views.contact,name="contact"),
path("onepiece",views.onepiece,name="onepiece"),
path("naruto",views.naruto,name="naruto"),
path("demonslayer",views.demonslayer,name="demonslayer"),

]
