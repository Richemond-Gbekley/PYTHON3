#Mapping url to view function
from django.urls import path
from .import views

#defining our special variables
#Url conf(configuration)
urlpatterns = [
    path('Home/',views.request)
]