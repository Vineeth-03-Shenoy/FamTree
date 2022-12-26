"""FamilyDBMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from famapp import views

admin.autodiscover()

urlpatterns = [
    path('', views.home, name="home"),
    path('famapp/home/',views.FamHome, name="famHome"),
    path('famapp/home/DataBase/',views.DataBase, name="DataBase"),
    path('famapp/home/Eventmanager/',views.eventmanager, name="Eventmanager"),
    path('famapp/home/DataBase/NewMember/',views.NewMember, name="NewMember"),
    path('famapp/home/DataBase/DeleteMember/',views.DeleteMember, name="DeleteMember"),
    path('famapp/home/DataBase/ViewPage/',views.ViewPage, name="ViewPage"),
    path('famapp/home/DataBase/ViewPage/Search/',views.ViewSearchPage, name="ViewSearchPage"),
    path('famapp/home/DataBase/ViewPage/DB/',views.ViewDBPage, name="ViewDBPage"),
    path('famapp/', include('famapp.urls')),
    path('admin/', admin.site.urls),
]
