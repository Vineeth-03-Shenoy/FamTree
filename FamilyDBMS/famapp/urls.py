
from django.urls import include, path
from . import views

app_name = 'famapp'

urlpatterns = [
    path('', views.home, name="home"),
    path('home/',views.FamHome, name="famHome"),
    path('accounts/', include('accounts.urls')),
]
