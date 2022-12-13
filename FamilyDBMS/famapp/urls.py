
from django.urls import include, path
from . import views

app_name = 'famapp'

urlpatterns = [
    path('', views.home),
    path('accounts/', include('accounts.urls')),
]
