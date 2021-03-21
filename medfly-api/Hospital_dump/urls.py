from django.contrib import admin
from django.urls import path
from . import views 
from . import hospitals, procedures_view


urlpatterns = [
    
    path('', views.dashboard),
     

]
