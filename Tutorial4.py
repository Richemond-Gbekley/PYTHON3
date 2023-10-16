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