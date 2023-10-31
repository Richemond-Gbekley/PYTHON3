#Mapping url to view function
from django.urls import path
from .import views 


#defining our special variables
#Url conf(configuration)
urlpatterns = [
   # path('Home/', views.request),
     path('Home/', views.Home, name='Arduino_Home'),
     path('Order/', views.My_Order, name='Arduino_Order'),
     path('About/',views.About, name = 'Arduino_About'),
     #  path('', views.request, name='request'),
    
     
]