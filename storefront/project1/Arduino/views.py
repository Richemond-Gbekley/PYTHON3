from django.shortcuts import render
from django.http import HttpResponse #Since we are looking at a request , and we are expecting a response, we are supponsed to import the response class from http package
from django.template import loader
from .models import Order



# Create your views here.

#Takes a request -> returns a response
#More accurately its a request handler or action in some frame works

def Home(request) :                  #This function is taking a request object and return a response
      #We can do a lot with this request function
      #We can pull data
      #We can transform data
      #We can send emails                                  
      return HttpResponse('YOUR WORLD OF ARDUINO')  #Creating an instance of the http response class
  
                         #After we mark this view to url, so that when we get a request on that url , a fuction would be called.
                           
      #return render(request, 'Home.html')                  #Using html templates
 #return render(request, 'Arduino/Templat_Home.html')
 
  #return render(request, 'Arduino/Home.html')
def My_Order(request):
      my_order = Order.objects.all().values()
      template = loader.get_template('Order.html')
      context = {'Order':my_order,}
      return HttpResponse(template.render(context, request))

def About(request):
      return render(request, 'About.html')
