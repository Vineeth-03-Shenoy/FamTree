
from django.urls import include, path
from . import views

app_name = 'famapp'

urlpatterns = [
    path('', views.home, name="home"),
    path('home/',views.FamHome, name="famHome"),
    path('home/DataBase/', views.DataBase, name="DataBase"),
    path('home/DataBase/NewMember/',views.NewMember, name="NewMember"),
    path('home/DataBase/DeleteMember/',views.DeleteMember, name="DeleteMember"),
    path('home/DataBase/ViewPage/',views.ViewPage, name="ViewPage"),
    path('home/DataBase/ViewPage/SearchID/',views.ViewSearchIDPage, name="ViewSearchIDPage"),
    path('home/DataBase/ViewPage/SearchName/',views.ViewSearchNamePage, name="ViewSearchNamePage"),
    path('home/DataBase/ViewPage/DB/',views.ViewDBPage, name="ViewDBPage"),
    path('accounts/', include('accounts.urls')),
]
