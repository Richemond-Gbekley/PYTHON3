"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path  # if you want to include another url conf, you add include just after the import path
from django.urls import include, path
urlpatterns = [
   path('admin/', admin.site.urls),
    path('Arduino/Home',include('Arduino.urls')),#You also add the url here
    path('', include('Arduino.urls')),
    
]

#It looks like you've made progress! The error message you're seeing now is a standard 404 page, 
# which means that Django is correctly recognizing your project's URL patterns.
#The issue seems to be that you don't have a URL pattern defined for the root URL.
# To fix this, you need to add a pattern for the empty path in your urls.py file.
#In your project1/urls.py file, you can do something like this: