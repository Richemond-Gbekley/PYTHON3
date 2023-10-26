from django.db import models

# Create your models here.

class Order (models.Model) :
   Product_Name = models.CharField ( max_length=255)
   #Price = models.DecimalField(max_digits=10, decimal_places=2)
   Name = models.CharField (max_length=255)              #py manage.py makemigrations Arduino: To create a database 
   Date = models.DateField(auto_now=True)        #Django creates a file describing the changes and stores the file in the /migrations/ folder:
                                                #py manage.py migrate :  Django will create and execute an SQL statement,
                                                # based on the content of the new file in the /migrations/ folder.
                                                #View SQL
                                               #As a side-note: you can view the SQL statement that were executed from the migration above. 
                                               # All you have to do is to run this command, with the migration number:py manage.py sqlmigrate Arduino 0001
                            #Add Records
#The Members table created in the previous chapter is empty.
#We will use the Python interpreter (Python shell) to add some members to it.
#To open a Python shell, type this command: py manage.py shell
#>>> from Arduino.models import Order
#>>> Order.objects.all()
#>>> order = Order(Product_name='Uno', Product_Price=10.5, Name="Grey")
#>>> Arduino.save()
#>>> Order.objects.all().values() : To view the table

#to update and pull data
#>>> from Arduino.models import Order
#>>> x = Order.objects.all()[4]
# x will now represent the member at index 3, which is "Reen", but to make sure, let us see if that is correct:
#x.Name

#Delete
#>>> x.delete()