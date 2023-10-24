#Functions
#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.

#In Python a function is defined using the def keyword:

def my_fucntion() :

 print (" its my function")

my_fucntion()


#Arguments
#Information can be passed into functions as arguments.
#Arguments are specified after the function name,
# inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
#The following example has a function with one argument (request). 
# When the function is called, we pass along a first name, which is used inside the function to print the full name:

print("\n")
print("Functions with argument")
print("***********************")
def request(request):
    print(request)
    
request("Pull database")                # From a function's perspective:
request('Transfer database')             #******************************
request('view Home page')                                #A parameter is the variable listed inside the parentheses in the function definition.
                                #An argument is the value that is sent to the function when it is called.

#Number of Arguments
#By default, a function must be called with the correct number of arguments.
# Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.


#Lambda
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression
print("\n")
print("Lambda")
print("*******")
x = lambda  a : a + 10 
print(x(5))



#Why Use Lambda Functions?
#The power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
print("\n")
print("Using ananymously inside a function")
print("***********************************")
def myfunc(n) :
    return lambda a : a + n 
represent_lambda = myfunc(3)
print(represent_lambda(3))



#Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

#Classes/Object 
#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.

#To create a class, use the keyword class:
print("\n")
print("Creating a class")
class myclass :
    b = 5 
    print(b)
    

    
    
    #Now we can use the class named MyClass to create objects:
    print("\n")
    print("Creating object")
p = myclass()
print(p.b)


#The __init__() Function
#The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
#To understand the meaning of classes we have to understand the built-in __init__() function.
#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
print("\n")            
print("Class and Object plus init function")                    
class Cybersecurity :
     def __init__(self, Field , level) :
         self.Field = Field
         self.level = level
     
O = Cybersecurity("Ethical Hacking" , "level1" ) 
print(O.Field)
print(O.level)

#The __str__() Function
#The __str__() function controls what should be returned when the class object is represented as a string.
#If the __str__() function is not set, the string representation of the object is returned:

print("\n")            
print("Class and Object plus init function and string function")                    
class Cybersecurity :
     def __init__(self, Field , level) :
         self.Field = Field
         self.level = level
         
     def __str__(self) :
      return f"{self.Field}{self.level}"
    
     
O = Cybersecurity("Ethical Hacking  :" ," Level 1")
print(O)


#Object Methods
#Objects can also contain methods. Methods in objects are functions that belong to the object.
#Let us create a method in the Person class:
print("\n")
print("object method")
class Cybersecurity :
    def __init__(self, field , level ) :
        self.field = field
        self.level = level
        
    def myfunc(self) :
            print("Your field  is  " + self.field , "and your level is " + self.level)
    
o = Cybersecurity("Ethical Hacking" , "Level1")
o.myfunc()
     
     
   #  The self Parameter
#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

#Inheritance 
#inheritance allows us to define a class that inherits all the methods and properties from another class

#Parent class is the class being inherited from , also called base class 
#Child class is the class that inherits from another class, also called derived class

#CREATE A PARENT CLASS
#Any class can be parent class, so the syntax is the same as creating any other class

print("\n")
print("Creating a parent class")
print("************************")
class Electronic_device :
    def __init__(self, Product , Price ) :
        self.product = Product 
        self.price = Price
        
    def printresult(self) :
            print(self.product , self.price)
            
O1 = Electronic_device ("Module charger  :" , 100)
O1.printresult()      


# Creating a child class 
#To create a class that inherits the functionality from another class, send the parent class as a parameter
#when creating the child class
print("\n")
print("Creating a child class without adding properties and method")
print("**************************************************************")
class Arduino (Electronic_device) :
    pass

#Note : use the pass keyword when you do not want to add any other properties or methods to the class.
O2 = Arduino ("Arduino uno : " , 150)
O2.printresult()

print("\n")
print("Creating a child class, adding properties and method")
print("******************************************************")
class Arduino (Electronic_device) :                     #To add the init function, it means adding new properties, but also the child class 
    def __init__(self, Product, Price, Module):         #will no longer inherit the parents init function
        super().__init__(Product, Price)          #Note : To keep the inheritance of the parents init function, add a call to the parents init function
        self.module = Module 
    def result(self) :
            print(self.product ,":", self.price ,":", self.module)
#Note : use the pass keyword when you do not want to add any other properties or methods to the class.
O2 = Arduino ("Arduino uno" , 150 , 2017)
O2.result()

#Iterators 
#Is an object that contains a countable number of values 
#An iterator is an object that can be iterated upon, meaning that you can traverse through all the values

#Technically, in python , an iterator is an object which implements the iterator protocol, which consists of the methods 
#iter() and next() 

#Note : Iterable is the object that contains a number of countable values , where as iterators counts this values.
#an example of iterables are list , tuples ,strings, set etc 
print("\n")
print("Iterator")
print("*********")
mytuple = ("Ethical Hacking " , "Web exploitation" ,"Crytography")
it = iter(mytuple)
print(next(it))
print(next(it))
print(next(it))

print("\n")
print("Looping through an iterable")
print("****************************")
for x in mytuple :
    print(x)
    
    
    #Creating an iterator
    #To create an object/class as an iterator you have to implement to methods 
    #iter () and next () to your object.
    #the iter () methods helps to do some operations but also returns the iterator object itself 
    #The next() method also allows some operations and must return the next item in the sequence
    
print("\n")
print("Creating an Iterator")
print("*********************")
class MyNumbers :
    def __iter__(self) :
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a 
        self.a += 1 
        return x
Object_Mynumber = MyNumbers()
myit = iter(Object_Mynumber)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


#Stop iteartor

print("\n")
print("Stopping  an Iterator")
print("*********************")
class MyNumber :
    def __iter__(self) :
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 10 :
         x = self.a 
         self.a += 1 
         return x
        else :
         raise StopIteration
    
Object_Mynumb = MyNumber()
myit = iter(Object_Mynumb)
for x in myit :
    print(x)
    
    #Polymorphism 
    #Is used in class methods, where we can have multiple classes with the same method name
    
print("\n")
print("Polymorphism")
print("*************")    
class email :
    def __init__(self, email) :
        self.email = email 
        
    def result(self) :
            print(self.email) 
           
class Name :            
    def __init__(self,Fname ,Sname) :
        self.fname = Fname 
        self.sname = Sname
         
    def result (self) :
        print(self.fname , self.sname)
     
class contact :
    def __init__(self, contact) :
        self.contact = contact 
        
    def result(self) :
            print(self.contact) 
            
Object1 = email ("hackathon1234@hackathon.com")
Object2 = Name ("Hackathon" , "Gameover")
Object3 = contact ("+44498976876987")

for x in (Object1,Object2,Object3) :
    x.result()
                 
                 #Module
print("\n") 
print("Module in Python") 
print("*****************")               
import mymodule
mymodule.greetings("Hackathon")

#Renaming a module 
#You can create an alias when you import a module , by using the as keyword 
print("\n") 
print("Renaming Module in Python") 
print("***************************") 
import mymodule as mm 
mm.greetings("Gameover")

print("\n") 
print("Module in Python") 
print("*****************") 
import platform           #the module platform is an in built function in python and it prints out the OS been used 
x = platform.system()
print(x)

print("\n") 
print("Module in Python") 
print("*****************")
import platform           #the dir , would print all the variables names in the module 
x = dir (platform)
print(x)


print("\n") 
print("Module in Python") 
print("*****************")    # the output shows the variable name greetings we created 
x = dir(mymodule)
print(x)

#Date time 
#its also a module
print("\n") 
print("Date and time in  python") 
print("************************") 
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

print("\n") 
print("Date and time in python") 
print("************************") 
import datetime
x = datetime.datetime(2023,10,5)
print(x)


#Python try except
#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The else block lets you execute code when there is no error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks

print("\n") 
print("Try and except in python") 
print("*************************")
try :
     print(a) 
except :
     print("Bruh , a was not defined")
     
print("\n") 
print("Try and except in python") 
print("*************************")
try : 
    file = open("myfile.txt") 
    try:
        file.write("im writing into the file")
    except :
        print("Do you really have this file")
    finally :
        file.close()
except :
     print("check your file system")
    
    
#Raise an exception
#You can choose to throw an exception if a condition occurs.
#To throw (or raise) an exception, use the raise keyword.
print("\n") 
print("Raise an exception") 
print("******************")
q = 1
if  q < 2 :
   raise Exception("sorry , no number below 1")
print("******************************************")
print("\n") 
print("Raise an exception") 
print("******************")

dial = "*170# "

if not type(dial) is  int :
    raise TypeError("Integers only")


#User Input
print("\n") 
print("User input") 
print("***********")
dial_code = input("Dial *170# to enjoy exciting offers \n ")

