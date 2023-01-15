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
    path('famapp/home/TraceTree/',views.Famtree, name="TraceTree"),
    path('famapp/home/About/',views.About, name="About"),
    path('famapp/home/Contact/',views.Contact, name="Contact"),
    path('famapp/home/Eventmanager/',views.eventmanager, name="Eventmanager"),
    path('famapp/home/Eventmanager/NewEvent/',views.Newevent, name="NewEvent"),
    path('famapp/home/Eventmanager/DeleteEvent/',views.DeleteEvent, name="DeleteEvent"),
    path('famapp/home/Eventmanager/Invitees/',views.Invited, name="Invitees"),
    path('famapp/home/Eventmanager/ViewInvitees/',views.ViewInvitees, name="ViewInvitees"),
    path('famapp/home/Eventmanager/All_Events/',views.AlleventsDisplay, name="AllEvents"),
    path('famapp/home/DataBase/NewMember/',views.NewMember, name="NewMember"),
    path('famapp/home/DataBase/DeleteMember/',views.DeleteMember, name="DeleteMember"),
    path('famapp/home/DataBase/ViewPage/',views.ViewPage, name="ViewPage"),
    path('famapp/home/DataBase/PersonalInfo/',views.personalInfoInsert, name="PersonalInfo"),
    path('famapp/home/DataBase/PersonalInfo/personalInfoSearch',views.personalInfoSearch, name="personalInfoSearch"),
    path('famapp/home/DataBase/ViewPage/SearchID/',views.ViewSearchIDPage, name="ViewSearchIDPage"),
    path('famapp/home/DataBase/ViewPage/SearchName/',views.ViewSearchNamePage, name="ViewSearchNamePage"),
    path('famapp/home/DataBase/ViewPage/SearchParents/',views.ViewSearchParents, name="ViewSearchParents"),
    path('famapp/home/DataBase/ViewPage/SearchChildren/',views.ViewSearchChildren, name="ViewSearchChildren"),
    path('famapp/home/DataBase/ViewPage/DB/',views.ViewDBPage, name="ViewDBPage"),
    path('famapp/home/DataBase/ViewPage/CoupleDB/',views.ViewCoupleDB, name="ViewCoupleDB"),
    path('famapp/home/DataBase/ViewPage/ParentsDB/',views.ViewParentsDB, name="ViewParentsDB"),
    path('famapp/home/DataBase/ViewPage/FamiliesDB/',views.ViewFamilies, name="ViewFamilies"),
    path('famapp/home/DataBase/UpdateDetails/',views.UpdateDetails, name="UpdateDetails"),
    path('famapp/home/DataBase/CoupleRegister/',views.insertCoupleInfo,name="InsertCouple"),
    path('famapp/home/DataBase/ParentsRegister/',views.insertParentsInfo,name="InsertParent"),
    path('famapp/', include('famapp.urls')),
    path('admin/', admin.site.urls),
]
